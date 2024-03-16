from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from personal_streamlit.llm.openai import get_chat_model


def get_chat_chain():
    prompt = ChatPromptTemplate.from_template("User: {input}")
    model = get_chat_model()
    output_parser = StrOutputParser()
    return prompt | model | output_parser
