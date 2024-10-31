import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(page_title="Simple convo", page_icon="📈")

st.markdown("# Simple convo")
st.sidebar.header("Simple convo")
st.write("""Simple request - response""")
