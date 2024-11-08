import streamlit as st
from random_file import another_page_from_another_py

def another_page():
    st.write("This is another page")


st.image("logo.jpeg", use_container_width=True)

pages = {
    "Theorems": [
        st.Page("thevenins.py", title="Thevenin's theorem"),
        st.Page("nortons.py", title="Norton's theorem"),
    ],
    "Circuits": [
        st.Page(another_page, title="Another page"),
        st.Page(another_page_from_another_py, title="Another page from another.py"),
    ],
}

pg = st.navigation(pages)
pg.run()
