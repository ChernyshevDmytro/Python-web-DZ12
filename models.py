from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import DateTime

from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base() 

class Price(Base):
    __tablename__ = "prices"    
    id = Column(Integer, primary_key=True)
    brain_price = Column(Integer)
    telemart_price = Column(Integer)
    compx_price = Column(Integer)
    created_at = Column(DateTime) 
