import streamlit as st
import requests
import os
import re
from dotenv import load_dotenv

# השתמש ב-PAT שלך במשתנה סביבה
# TOKEN = os.getenv("GITHUB_TOKEN")  # הגדר GITHUB_TOKEN במערכת

st.set_page_config(page_title="חיפוש בקוד של המורה", page_icon="🔍")
st.title("🔍 חיפוש בקוד של pythonai250824 עם תצוגה מקדימה")
st.write("תוכל לראות קטעי קוד סביב מילת החיפוש (3 שורות לפני ואחרי)")

# קלט מהמשתמש
query = st.text_input("מה ברצונך לחפש?")

search_scope = st.radio(
    "בחר תחום חיפוש:",
    ["🔹 כל הקבצים", "🐍 קבצי Python בלבד", "📘 מדריכים (Markdown) בלבד"],
    index=0,
)

if st.button("בצע חיפוש") and query.strip():
    # בונים שאילתא
    q = f"user:pythonai250824 {query}"
    if search_scope == "🐍 קבצי Python בלבד":
        q += " language:python"
    elif search_scope == "📘 מדריכים (Markdown) בלבד":
        q += " extension:md"

    # בקשת חיפוש
    url = "https://api.github.com/search/code"
    params = {
        "q": q,
        "per_page": 20,
        "sort": "indexed",  # סדר לפי אינדקס GitHub
        "order": "asc"  # מהישן לחדש
    }

    load_dotenv()
    TOKEN = os.getenv("GITHUB_TOKEN")
    headers = {
        "Accept": "application/vnd.github.v3.text-match+json",
        "Authorization": f"token {TOKEN}"
    }

    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        results = response.json().get("items", [])
        if results:
            st.success(f"נמצאו {len(results)} תוצאות:")
            for item in results:
                name = item['name']
                path = item['path']
                repo = item['repository']['full_name']
                html_url = item['html_url']
                raw_url = item['url']  # זה הקובץ API נכון
                raw_headers = {"Authorization": f"token {TOKEN}"}
                raw_resp = requests.get(raw_url, headers=raw_headers)

                st.markdown(f"### [{name}]({html_url}) ב־`{repo}/{path}`")

                # הורדת הקובץ הגולמי
                raw_headers = {"Authorization": f"token {TOKEN}"}
                raw_resp = requests.get(raw_url, headers=raw_headers)
                if raw_resp.status_code == 200:
                    content = raw_resp.json().get("content", "")
                    import base64
                    code_text = base64.b64decode(content).decode('utf-8', errors='ignore')
                    # מציאת קטע סביב מילת החיפוש
                    lines = code_text.splitlines()
                    matches = [i for i, line in enumerate(lines) if re.search(query, line, re.IGNORECASE)]
                    for idx in matches:
                        start = max(idx - 3, 0)
                        end = min(idx + 4, len(lines))
                        snippet = "\n".join(lines[start:end])
                        # החלפה של מילת החיפוש עם <mark>
                        # הדגשת מילת החיפוש עם רקע צהוב
                        highlighted_snippet = re.sub(
                            f"({re.escape(query)})",
                            r'<mark style="background-color: yellow; color: black;">\1</mark>',
                            snippet,
                            flags=re.IGNORECASE
                        )
                        st.markdown(f"<pre>{highlighted_snippet}</pre>", unsafe_allow_html=True)


                else:
                    st.info("לא ניתן להוריד את הקובץ להצגת תצוגה מקדימה.")
        else:
            st.info("לא נמצאו תוצאות עבור החיפוש הזה.")
    else:
        st.error(f"שגיאה ב־API: {response.status_code}")
