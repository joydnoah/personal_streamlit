from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from personal_streamlit.db.models.base import Base


class Curriculum(Base):
    __tablename__ = "curriculum"

    uuid: Mapped[str] = mapped_column(primary_key=True)
    profile_name: Mapped[str] = mapped_column()
    information: Mapped[str] = mapped_column()
    created_at: Mapped[datetime] = mapped_column()

    def __repr__(self) -> str:
        return f"Curriculum({self.uuid}, {self.profile_name})"
