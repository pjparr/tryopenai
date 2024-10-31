import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Streamlit! 👋")

st.sidebar.success("Select one of the above.")

st.markdown(
    """
    Using streamlit to consume Hugging Face API
    """
)
