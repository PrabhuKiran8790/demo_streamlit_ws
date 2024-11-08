import streamlit as st


def another_page_from_another_py():
    st.write("this is from another page")

    checkbox_clicked = st.checkbox("Click me")

    st.write("Checkbox clicked:", checkbox_clicked)

    if checkbox_clicked:
        pass
        # do something