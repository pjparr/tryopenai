## Course from deeplearning.ai
# https://python.langchain.com/docs/integrations/chat/huggingface/

import json
from typing import Any, Iterable, LiteralString
from huggingface_hub.inference._generated.types.chat_completion import (
    ChatCompletionStreamOutput,
)
from huggingface_hub import InferenceClient

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain.prompts import ChatPromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

from langchain_huggingface.embeddings import (
    HuggingFaceEmbeddings,
)  ### dont import import HF stuff from langchain (this is all deprecated)


from langchain_community.document_loaders import CSVLoader
from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain_community.llms import huggingface_hub
from IPython.display import display, Markdown
from langchain.chains import RetrievalQA

#### for some sample data
import pandas as pd

# create a generic config and pass this to the get_resp function
chat_config: dict[str, Any] = {
    "temperature": 0.0,
    "model": "HuggingFaceH4/starchat2-15b-v0.1",
    "max_tokens": 1024,
    "top_p": 0.7,
}

client = InferenceClient(api_key="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")


## here messages is the entire message history
def get_a_resp(messages: list):  ##### list of dict values
    """_summary_

    Args:
        theprompt (str): _description_
        messages (list): _description_

    Yields:
        _type_: _description_
    """
    ## perhaps need to do a deep copy ??
    # newlist: list = [
    #     {"role": item["role"], "content": item["content"]} for item in messages
    # ]

    # stream: Iterable[ChatCompletionStreamOutput] = client.chat.completions.create(
    #     model="HuggingFaceH4/starchat2-15b-v0.1",
    #     messages=newlist,
    #     temperature=0.5,
    #     max_tokens=1024,
    #     top_p=0.7,
    #     stream=True,
    # )
    stream: Iterable[ChatCompletionStreamOutput] = client.chat.completions.create(
        messages=messages,
        stream=True,
        **chat_config,
    )

    # Still streaming the individual words (the streamer would appear to add spaces between)
    for chunk in stream:
        yield chunk.choices[0].delta.content

        ### (remember this turns a normal fucntion into a generator function)


def lesson_0():
    # init messages
    messages: list[dict] = []  # is a list of dict of items with role and content

    while True:
        prompt = input(
            "tell me whats happening? (type END when done with this conversation)"
        )
        messages.append({"role": "user", "content": prompt})

        # for chunk in get_a_resp(prompt, messages):
        response = "".join([str(i) for i in get_a_resp(messages)])
        messages.append({"role": "assistant", "content": response})
        print(response)

        if prompt == "END":
            break


def lesson_1():
    messages: list[dict] = []  # is a list of dict of items with role and content

    ## Using a structured prompt template
    style: LiteralString = "Conversational"
    customer_email: str = "Something is wrong my blender!"
    prompt: str = f"""Translate the text \
    that is delimited by triple backticks 
    into a style that is {style}.    
    text: ```{customer_email}```
    """
    print(prompt)

    messages.append({"role": "user", "content": prompt})
    response = "".join([str(i) for i in get_a_resp(messages)])
    print(response)


def lesson_2():
    ## Using ChatPromptTempate

    prompt_template: str = """Translate the text \
    that is delimited by triple backticks 
    into a style that is {style}.    
    text: ```{text}```
    """
    print(prompt_template)

    templ = ChatPromptTemplate.from_template(prompt_template)

    style: LiteralString = "Conversational"
    customer_email: str = "Something is wrong my blender!"

    lang_messages = templ.format_messages(style=style, text=customer_email)

    messages: list[dict] = []
    messages.append({"role": "user", "content": lang_messages[0].content})

    response = "".join([str(i) for i in get_a_resp(messages)])
    print(response)


def lesson_3():
    ## instruction to extract specific informaton from the prompt ---- customer reviews

    customer_review = """\
    This leaf blower is pretty amazing.  It has four settings:\
    candle blower, gentle breeze, windy city, and tornado. \
    It arrived in two days, just in time for my wife's \
    anniversary present. \
    I think my wife liked it so much she was speechless. \
    So far I've been the only one using it, and I've been \
    using it every other morning to clear the leaves on our lawn. \
    It's slightly more expensive than the other leaf blowers \
    out there, but I think it's worth it for the extra features.
"""

    prompt_template = """\
    For the following text, extract the following information:

    gift: Was the item purchased as a gift for someone else? \
    Answer True if yes, False if not or unknown.

    delivery_days: How many days did it take for the product \
    to arrive? If this information is not found, output -1.

    price_value: Extract any sentences about the value or price,\
    and output them as a comma separated Python list.

    Format the output as JSON with the following keys:
    gift
    delivery_days
    price_value

    text: {text}
    """

    templ = ChatPromptTemplate.from_template(prompt_template)

    lang_messages = templ.format_messages(text=customer_review)

    messages: list[dict] = []
    messages.append({"role": "user", "content": lang_messages[0].content})

    response = "".join([str(i) for i in get_a_resp(messages)])
    print("Here is the reponse:", response)

    # convert to a dictionary
    response_dict = json.loads(response)
    print("gift:", response_dict["gift"])
    print("delivery_days:", response_dict["delivery_days"])
    print("price_value:", response_dict["price_value"])

    # Presentingg the output in a better way
    #### set up a parser
    from langchain.output_parsers import ResponseSchema
    from langchain.output_parsers import StructuredOutputParser

    # handling the output
    gift_schema = ResponseSchema(
        name="gift", description="Was this review given as a gift?"
    )
    delivery_days_schema = ResponseSchema(
        name="delivery_days",
        description="How many days did it take for the product to arrive?",
    )
    price_value_schema = ResponseSchema(
        name="price_value",
        description="Extract any sentences about the value or price, and output them as a comma separated Python list",
    )

    output_parser = StructuredOutputParser.from_response_schemas(
        [gift_schema, delivery_days_schema, price_value_schema]
    )

    out_dict = output_parser.parse(response)
    print(out_dict)


def lesson_4():
    llm_model = "HuggingFaceH4/starchat2-15b-v0.1"

    llm = HuggingFaceEndpoint(
        repo_id="microsoft/Phi-3-mini-4k-instruct",
        task="text-generation",
        max_new_tokens=512,
        do_sample=False,
        repetition_penalty=1.03,
    )  # type: ignore

    # llm = ChatHuggingFace(temperature=0.0, model=llm_model)
    memory = ConversationBufferMemory()
    conversation = ConversationChain(llm=llm, memory=memory, verbose=False)
    conversation.predict(input="Hi, my name is Jack")
    conversation.predict(input="What is 1+1?")
    conversation.predict(input="What is my name?")
    memory.load_memory_variables({})
    memory.save_context({"input": "Hi"}, {"output": "What's up"})
    print(conversation)

    ##### remember call to the LLM are stateless - appear to have memory

    ###### how else can you store memory --- ConversationBufferMemory
    ####### ConversationBufferWindowMemory --- only the most recent exchanges are stored??   -- only stores the most recent exchange


def lesson_5():
    #### what are embeddings

    ## embeding vector captues the meaning of data, AND
    ## text with similar content will have similar embeddings / vectors

    ### doc -> chunks -> embeddings

    # # # from langchain.prompts import PromptTemplate
    # # # from langchain.memory import ConversationBufferMemory

    print("Success")

    ## use our sample file
    file = ".\student_lifestyle_dataset.csv"

    # test if a file exists
    import os

    if os.path.exists(file):
        print("file exists")
    else:
        print("file does not exist")
        exit()

    loader = CSVLoader(file_path=file)
    docs = loader.load()
    # print(docs[0])

    embeddings = HuggingFaceEmbeddings()  ##
    db: DocArrayInMemorySearch = DocArrayInMemorySearch.from_documents(docs, embeddings)

    query = (
        "Please list the students having the 3 highest number of study hours per day"
    )

    docs = db.similarity_search(query)

    print("The number of docs returned is:", len(docs))

    print(display(docs[0]))

    print("success")


lesson_5()
