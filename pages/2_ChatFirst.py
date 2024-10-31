import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(page_title="First attempt", page_icon="📈")

st.markdown("# First attempt")
st.sidebar.header("First attempt")
st.write("""Simple request - response""")


# create a side to show subpages


def get_a_resp(theprompt: str):
    client = InferenceClient(api_key=st.secrets["hf_key"])
    messages = [{"role": "user", "content": theprompt}]
    stream = client.chat.completions.create(
        model="HuggingFaceH4/starchat2-15b-v0.1",
        messages=messages,
        temperature=0.5,
        max_tokens=1024,
        top_p=0.7,
        stream=True,
    )

    streamlist = []
    for chunk in stream:
        streamlist.append(chunk.choices[0].delta.content)

    return " ".join(streamlist)


def on_click_cb(theprompt):
    print(f"Doing on click{theprompt}\n")
    # resp_text = resp()
    # print(resp_text)


# Show textbox, submit and result


def handle_form_submit():  # button click
    st.session_state.submission = st.session_state.FORM_INPUT


def handle_on_change():
    print("dong on change")
    if st.session_state.FORM_INPUT:
        st.session_state.has_value = True


def handle_sidebar_first():
    print("show first page")


if "has_value" not in st.session_state:
    st.session_state.has_value = False
if "reply" not in st.session_state:
    st.session_state.thereply = ""
st.title("Test out text completion")

val = st.text_input(
    "Ask me something...", value="", on_change=handle_on_change, key="FORM_INPUT"
)
submit_button = st.button(
    label="Submit", disabled=not st.session_state.has_value, on_click=handle_form_submit
)
if submit_button:
    print("is clicked")
    reply = get_a_resp(st.session_state.submission)
    st.session_state.thereply = reply

st.text_area("Here is the response", value=st.session_state.thereply, key="REPLY")
