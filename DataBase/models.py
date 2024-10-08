from sqlalchemy import Column, BigInteger, Integer
from .database import Base, engine


class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    onewin_id = Column(BigInteger, nullable=False)
    tg_id = Column(BigInteger, nullable=True)


Base.metadata.create_all(bind=engine)
