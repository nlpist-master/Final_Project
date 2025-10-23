import streamlit as st
import urllib.parse
import webbrowser

st.set_page_config(page_title="חיפוש בקוד של המורה", page_icon="🔍")

st.title("🔍 חיפוש בקוד של pythonai250824")
st.write("חפש לפי נושא וראה באיזה שיעור זה מופיע בקוד או בהסברים.")

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
        # בונים את השאילתא לפי סוג הבחירה
        base_query = f"user:pythonai250824 {query}"
        if search_scope == "🐍 קבצי Python בלבד":
            base_query += " language:python"
        elif search_scope == "📘 מדריכים (Markdown) בלבד":
            base_query += " extension:md"

        # קידוד ל־URL
        encoded_query = urllib.parse.quote(base_query)
        url = f"https://github.com/search?q={encoded_query}"

        # תוצאה
        st.success("פותח את תוצאות החיפוש בגיטהאב...")
        webbrowser.open_new_tab(url)
    else:
        st.warning("אנא הזן נושא לחיפוש.")
