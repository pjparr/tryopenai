import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(page_title="Convert to image", page_icon="📈")

st.markdown("# Convert to image")
st.sidebar.header("Convert to image")
st.write("""Simple request - Convert to image""")
