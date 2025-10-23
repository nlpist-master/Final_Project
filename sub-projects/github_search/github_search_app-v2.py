import streamlit as st
import requests
import os
from dotenv import load_dotenv

# כותרת
st.set_page_config(page_title="חיפוש בקוד של המורה", page_icon="🔍")
st.title("🔍 חיפוש בקוד של pythonai250824")
st.write("חפש נושאים ותראה את תוצאות החיפוש ישירות כאן.")

# שדה קלט
query = st.text_input("מה ברצונך לחפש? (למשל: list comprehension, מחלקות, חריגות וכו׳)")

# בחירה בין סוגי קבצים
search_scope = st.radio(
    "בחר תחום חיפוש:",
    ["🔹 כל הקבצים", "🐍 קבצי Python בלבד", "📘 מדריכים (Markdown) בלבד"],
    index=0,
)

# כפתור חיפוש
if st.button("בצע חיפוש"):
    if query.strip():
        # בונים את השאילתא
        q = f"user:pythonai250824 {query}"
        if search_scope == "🐍 קבצי Python בלבד":
            q += " language:python"
        elif search_scope == "📘 מדריכים (Markdown) בלבד":
            q += " extension:md"

        # API של GitHub
        url = "https://api.github.com/search/code"
        params = {"q": q, "per_page": 20}  # 20 תוצאות לדוגמה
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
                    st.markdown(f"- **{name}** ב־`{repo}/{path}` ➡️ [צפה בקובץ]({html_url})")
            else:
                st.info("לא נמצאו תוצאות עבור החיפוש הזה.")
        else:
            st.error(f"שגיאה ב־API: {response.status_code}")
    else:
        st.warning("אנא הזן נושא לחיפוש.")
