import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

title = os.environ.get("TITLE")

st.title(f"{title}")
