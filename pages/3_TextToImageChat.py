import streamlit as st
import requests
import io
from PIL import Image
from huggingface_hub import InferenceClient
import os

################################################################################
## Text to image with chat
################################################################################

# Select a model (later get the full list of models)
model_options = [
    "Select",
    "black-forest-labs/FLUX.1-dev",
    "stabilityai/stable-diffusion-3-medium-diffusers",
]

st.set_page_config(page_title="Text to Image", page_icon="📈")
st.sidebar.header("Text to Image")
st.write("""Simple request - response""")
st.title("Text to image - no variations")


if "model_selection_index" not in st.session_state:
    st.session_state.model_selection_index = 0

model_option = st.selectbox(
    "Which model do you wish to use?",
    model_options,
    index=st.session_state.model_selection_index,
)
st.session_state.model_selection_index = model_options.index(model_option)


################################################################################
## Helper functions
################################################################################
def get_image_resp(payload):
    API_URL = f"https://api-inference.huggingface.co/models/{model_options[st.session_state.model_selection_index]}"
    headers = {"Authorization": f"Bearer {st.secrets["hf_key_read"]}"}

    # is there await / async concept in python?
    print(payload)
    # get the response
    response = requests.post(API_URL, headers=headers, json=payload)

    # create a temp file
    image = Image.open(io.BytesIO(response.content))
    image.save(f"./{st.session_state.image_counter}.png")

    return True


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
        st.session_state.messages.append(
            {"role": "assistant", "content": st.session_state.image_counter}
        )

        # display the above message
        st.chat_message("user").write(prompt)

        with st.spinner("Busy generating..."):
            # generate the image
            get_image_resp({"inputs": prompt})

        ## show the assistant prompt ONLY
        with st.chat_message("assistant"):
            image = Image.open(f"./{st.session_state.image_counter}.png")
            st.image(image)
