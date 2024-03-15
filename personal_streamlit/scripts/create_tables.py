from personal_streamlit.db.handlers.postgres import get_engine
from personal_streamlit.db.models.base import Base
from personal_streamlit.db.models.curriculum import Curriculum


def create_tables():
    engine = get_engine()
    Curriculum  # This is just for reference
    Base.metadata.create_all(engine)
