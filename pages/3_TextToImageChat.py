import streamlit as st
import requests
import io
from PIL import Image
from huggingface_hub import InferenceClient
import os


st.set_page_config(page_title="Text to Image", page_icon="📈")
st.sidebar.header("Text to Image")
st.write("""Simple request - response""")
st.title("Text to image - no variations")


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


# Select a model
model_option = st.selectbox()
    "Which model do you wish to use?",
    (
        "Select",
        "black-forest-labs/FLUX.1-dev",
        "stabilityai/stable-diffusion-3-medium-diffusers",
    ),
)

API_URL = f"https://api-inference.huggingface.co/models/{model_option}"
headers = {"Authorization": f"Bearer {st.secrets["hf_key_read"]}"}


def get_image_resp(payload):
    # is there await / async concept in python?
    print(payload)
    # get the response
    response = requests.post(API_URL, headers=headers, json=payload)

    # create a temp file
    image = Image.open(io.BytesIO(response.content))
    image.save(f"./{st.session_state.image_counter}.png")

    return True


################################################################################
## Text to image with chat
################################################################################


##############################################
## initialise messages
##############################################
if "messages" not in st.session_state:
    st.session_state.messages = []

    cmd = "del ?.png"
    returned_value = os.system(cmd)  # returns the exit code in Unix
    print("Returned value:", returned_value)

    st.session_state.image_counter = 0


for m in st.session_state.messages:
    if m["role"] == "user":
        st.chat_message(m["role"]).write(m["content"])
    if m["role"] == "assistant":
        ## check if file exists, if not show failed / interupted image
        print("checking path  ", f"./{m["content"]}.png")
        if os.path.exists(f"./{m["content"]}.png"):
            image = Image.open(f"./{m["content"]}.png")
            st.image(image)
        else:
            image = Image.open("./error.png")
            st.image(image)

if model_option != "Select":
    prompt = st.chat_input("Describe your desired image...")
    if prompt:
        st.session_state.image_counter = st.session_state.image_counter + 1

        # add to the messages store
        st.session_state.messages.append({"role": "user", "content": prompt})

        # display the above message
        st.chat_message("user").write(prompt)

        with st.spinner("Busy generating..."):
            # generate the image
            get_image_resp({"inputs": prompt})

        ## show the assistant prompt ONLY
        with st.chat_message("assistant"):
            image = Image.open(f"./{st.session_state.image_counter}.png")
            st.image(image)

        # below should be correct
        st.session_state.messages.append(
            {"role": "assistant", "content": st.session_state.image_counter}
        )
