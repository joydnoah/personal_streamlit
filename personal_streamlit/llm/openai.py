import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model = None


def get_chat_model():
    global model
    if not model:
        model = ChatOpenAI(model="gpt-4", openai_api_key=os.environ["OPENAI_API_KEY"])
        return model
    else:
        return model
