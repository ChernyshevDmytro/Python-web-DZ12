from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import DateTime

from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base() 

class Price(Base):
    __tablename__ = "prices"    
    id = Column(Integer, primary_key=True)
    sourse = Column(String(20), nullable=False)
    device = Column(String(50), nullable=False)
    price = Column(Integer)
    checked = Column(DateTime)
