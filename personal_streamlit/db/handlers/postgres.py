import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()


def get_engine():
    database_uri = os.environ["MAIN_DATABASE_URL"]
    return create_engine(database_uri, echo=True)
