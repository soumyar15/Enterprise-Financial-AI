from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String


class Base(DeclarativeBase):
    pass


class Portfolio(Base):

    __tablename__ = "portfolio"

    id = Column(Integer, primary_key=True)

    name = Column(String)

    value = Column(String)