import streamlit as st
import requests
import io
from PIL import Image
from huggingface_hub import InferenceClient

st.set_page_config(page_title="Text to Image", page_icon="📈")
st.sidebar.header("Text to Image")
#### use a dropdown to select either model
st.write("""Simple request - response""")
st.title("Test out text completion")


################################################################################
## Helper functions
################################################################################
def get_text_resp(theprompt: str):
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


API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
headers = {"Authorization": f"Bearer {st.secrets["hf_key_read"]}"}


def get_image_resp(payload):
    # is there await / async concept in python?
    print(payload)
    # get the response
    response = requests.post(API_URL, headers=headers, json=payload)

    # create a temp file
    image = Image.open(io.BytesIO(response.content))
    image.save("./tempimage.png")

    return True


# def handle_form_submit():  # button click
#     st.session_state.submission = st.session_state.FORM_INPUT


def handle_on_change():
    if st.session_state.FORM_INPUT:
        st.session_state.has_value = True


################################################################################
## Init streamlit state
################################################################################
st.session_state.submission = None
if "has_value" not in st.session_state:
    st.session_state.has_value = False
if "reply" not in st.session_state:
    st.session_state.thereply = ""


################################################################################
## Text to image
################################################################################
st.text_input(
    "Describe an image you want...",
    value="",
    on_change=handle_on_change,
    key="FORM_INPUT",
)
submit_button = st.button(label="Submit", disabled=not st.session_state.has_value)
if submit_button:
    # create JSON payload
    retn = get_image_resp(
        {
            "inputs": st.session_state.FORM_INPUT,
        }
    )
    st.session_state.thereply = "SUCCESS"


if st.session_state.thereply == "SUCCESS":
    image = Image.open("./tempimage.png")
    st.image(image, caption=f"Here is your picture - {st.session_state.FORM_INPUT}")

# if st.session_state.has_value:
#     st.write("Busy generating....")


### 