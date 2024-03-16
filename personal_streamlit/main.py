import os

import streamlit as st
from dotenv import load_dotenv

from personal_streamlit.chains.chat import get_chat_chain
from personal_streamlit.handlers.key_validator import is_valid_key

load_dotenv()

title = os.environ.get("TITLE")

st.title(f"{title}")

with st.sidebar:
    if "valid_key" not in st.session_state:
        key = st.text_input("Before anything please input the key:")
        if key:
            st.session_state.valid_key = is_valid_key(key)
    messages = st.container(height=300)
    if "valid_key" in st.session_state and st.session_state.valid_key:
        prompt = st.chat_input(placeholder="Your message")
        if prompt:
            chain = get_chat_chain()
            response = chain.invoke({"input": prompt})
            if "messages" in st.session_state:
                st.session_state.messages.append((prompt, response))
            else:
                st.session_state.messages = [(prompt, response)]

            if "messages" in st.session_state:
                for prompt, response in st.session_state.messages:
                    messages.chat_message("User").write(prompt)
                    messages.chat_message("Bot").write(response)
    elif "valid_key" in st.session_state and not st.session_state.valid_key:
        st.write("This is not a valid key.")
