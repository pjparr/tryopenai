import streamlit as st
import requests
import io
from PIL import Image

API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
headers = {"Authorization": f"Bearer {st.secrets["hf_key_read"]}"}


def get_image_resp(payload):
    # is there await / async concept in python?

    # get the response
    response = requests.post(API_URL, headers=headers, json=payload)

    # create a temp file
    image = Image.open(io.BytesIO(response.content))
    image.save("./tempimageTEST.png")

    return True


fn = get_image_resp(
    {
        "inputs": "can i have a picture of a shark",
    }
)

print(f"the return is {fn}")
