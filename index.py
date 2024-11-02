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

# Helper fucntions


def is_authenticated(user, password):
    if user == "Admin" and password == "12345678":
        return True
    else:
        return False


def linespace_generator(n_spaces=1):
    for i in range(n_spaces):
        st.write("")
