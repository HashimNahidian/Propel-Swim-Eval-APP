from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from db import Base

class Swimmer(Base):
    __tablename__ = "swimmers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)