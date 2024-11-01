import streamlit as st
from huggingface_hub import InferenceClient

client = InferenceClient(api_key=st.secrets["hf_key"])


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

    # Still streaming the individual words (the streamer would appear to add spaces between)
    for chunk in stream:
        yield chunk.choices[0].delta.content

        ### (remember this turns a normal fucntion into a generator function)


st.set_page_config(page_title="Simple convo", page_icon="📈")
st.markdown("# Simple chat UI - using HuggingFaceH4/starchat2-15b-v0.1")
st.sidebar.header("Simple chat UI")
st.write("""Simple LLM conversation with Streamlit widgets and Hugging Face""")

st.write(
    "DB username:",
)

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

    full_response = st.chat_message("assistant").write_stream(
        get_a_resp(prompt, st.session_state.messages)
    )

    # below should be correct
    st.session_state.messages.append({"role": "assistant", "content": full_response})

    ####

    # which model - check in sandbox ????
    # how to use streamlit chat message to display an image

    # can make a post to the endpoint
    # or use python client

# black-forest-labs/FLUX.1-dev: One of the most powerful image generation models that can generate realistic outputs.
# stabilityai/stable-diffusion-3-medium-diffusers: A powerful text-to-image model.
# variations - how can you change the image
