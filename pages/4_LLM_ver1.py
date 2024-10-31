import streamlit as st
from huggingface_hub import InferenceClient

client = InferenceClient(api_key="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")


## here messages is the entire message history
def get_a_resp(theprompt: str, messages: list):  ##### list of dict values
    ## perhaps need to do a deep copy ??
    newlist: list = [
        {"role": item["role"], "content": item["content"]} for item in messages
    ]

    stream = client.chat.completions.create(
        model="HuggingFaceH4/starchat2-15b-v0.1",
        messages=newlist,
        temperature=0.5,
        max_tokens=1024,
        top_p=0.7,
        stream=True,
    )

    return stream  #####   ?????
    ###### WE ARE NOT GOING TO DO THIS - perhaps would have to use yield
    # # streamlist = []
    # # for chunk in stream:
    # #     streamlist.append(chunk.choices[0].delta.content)

    # # return " ".join(streamlist)


st.set_page_config(page_title="Simple convo", page_icon="📈")
st.markdown("# Simple chat UI")
st.sidebar.header("Simple chat UI")
st.write("""Simple LLM conversation with Streamlit widgets""")

# session state - messages - will contain all the messages from user and assistant
if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    st.chat_message(m["role"]).write(m["content"])

prompt = st.chat_input("what happening??")
if prompt:
    # add to the messages store
    st.session_state.messages.append({"role": "user", "content": prompt})

    # display the above message
    st.chat_message("user").write(prompt)

    #### remember you need to send over everthing
    stream = client.chat.completions.create(
        model="HuggingFaceH4/starchat2-15b-v0.1",
        messages=[
            {"role": item["role"], "content": item["content"]}
            for item in st.session_state.messages
        ],
        temperature=0.5,
        max_tokens=1024,
        top_p=0.7,
        stream=True,
    )

    full_response = st.chat_message("assistant").write_stream(stream)

    # below should be correct
    st.session_state.messages.append({"role": "assistant", "content": full_response})
