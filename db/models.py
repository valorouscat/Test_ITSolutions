from sqlalchemy import Column, Integer, String

from .database import Base


class Item(Base):
    __tablename__ = "items"

    title = Column(String)
    id = Column(Integer, primary_key=True)
    author = Column(String)
    views = Column(Integer)
    position = Column(Integer)
