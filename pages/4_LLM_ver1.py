import streamlit as st
from huggingface_hub import InferenceClient
import numpy as np

st.set_page_config(page_title="Simple convo", page_icon="📈")

st.markdown("# Simple chat UI")
st.sidebar.header("Simple chat UI")
st.write("""Simple LLM conversation with Streamlit widgets""")

# use streamlits builtin widgets for chat message display
# chat input and chat message

# # with st.chat_message("user"):
# #     st.write("jkhkakjhdad")
# #     st.write("qqqqqq")
# # with st.chat_message("assistant"):
# #     st.write("test")

# # # add a simple bar chart
# # # # df = np.random.randn(10, 30)
# # # # with st.chat_message("user"):
# # # #     st.bar_chart(np.random.randn(30, 3))

# # prompt = st.chat_input("user")
# # if prompt:
# #     # if something entered do something
# #     st.write(f"adad {prompt}")

# session state - messages - will contain all the messages from user and assistant
if "messages" not in st.session_state:
    st.session_state.messages = []

# display the messages in chat_message
# message_list: list
# message_list = [
#     {"role": "user", "content": "ddddd"},
#     {"role": "assistant", "content": "3333ddddd"},
# ]
for m in st.session_state.messages:
    st.chat_message(m["role"]).write(m["content"])

prompt = st.chat_input("what happening??")
if prompt:
    # add to the messages store
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.messages.append({"role": "assistant", "content": prompt})

# could force a page reload

## how do you stream the prompt - responses
