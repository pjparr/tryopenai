"""
from langchain import PromptTemplate
from langchain.llms import OpenAI  ####  use hugging face
from langchain.chains import LLMChain

llm = OpenAI(temperature=0.9)
prompt = PromptTemplate(
    template="What is a good name for a company that makes {product}?",
    input_variables=["product"],
)
chain = LLMChain(llm=llm, prompt=prompt)
print(chain.run("colorful socks"))
"""

from typing import Iterable
from huggingface_hub.inference._generated.types.chat_completion import (
    ChatCompletionStreamOutput,
)
import streamlit as st
from huggingface_hub import InferenceClient

client = InferenceClient(api_key="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")


## here messages is the entire message history
def get_a_resp(theprompt: str, messages: list):  ##### list of dict values
    """_summary_

    Args:
        theprompt (str): _description_
        messages (list): _description_

    Yields:
        _type_: _description_
    """
    ## perhaps need to do a deep copy ??
    newlist: list = [
        {"role": item["role"], "content": item["content"]} for item in messages
    ]

    stream: Iterable[ChatCompletionStreamOutput] = client.chat.completions.create(
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


# init messages
messages: list[dict] = []  # is a list of dict of items with role and content

while True:
    prompt = input(
        "tell me whats happening? (type END when done with this conversation)"
    )
    messages.append({"role": "user", "content": prompt})

    # for chunk in get_a_resp(prompt, messages):
    response = "".join([str(i) for i in get_a_resp(prompt, messages)])
    print(response)
    messages.append({"role": "assistant", "content": response})

    if prompt == "END":
        break


## Langchain lesson 1
