import streamlit as st
import pandas as pd

st.set_page_config(page_title="Plot", page_icon="📈")
# st.markdown("# Plot")
st.sidebar.header("Plot")
st.write("""Simple demo of plotting functionality""")

df = pd.read_csv("./testdata.csv")
print(df)
st.bar_chart(df)
