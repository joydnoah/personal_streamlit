import os

import streamlit as st
from dotenv import load_dotenv

load_dotenv()

title = os.environ.get("TITLE")

st.title(f"{title}")
