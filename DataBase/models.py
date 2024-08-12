from sqlalchemy import Column, Integer
from .database import Base


class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    value = Column(Integer, nullable=False)
