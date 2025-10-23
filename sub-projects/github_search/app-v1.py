import streamlit as st
import urllib.parse
import webbrowser

st.set_page_config(page_title="חיפוש בקוד של המורה", page_icon="🔍")

st.title("🔍 חיפוש בקוד של pythonai250824")

st.write("הכנס נושא לחיפוש (למשל: 'list comprehension', או בעברית – 'לולאות', 'חריגות', 'מחלקות' וכו').")

# שדה קלט
query = st.text_input("מה ברצונך לחפש?")

# כפתור הפעלה
if st.button("בצע חיפוש"):
    if query.strip():
        # קידוד השאילתא ל-URL
        encoded_query = urllib.parse.quote(f"user:pythonai250824 {query}")
        url = f"https://github.com/search?q={encoded_query}"
        st.success("פותח את תוצאות החיפוש...")
        webbrowser.open_new_tab(url)
    else:
        st.warning("אנא הזן נושא לחיפוש.")
