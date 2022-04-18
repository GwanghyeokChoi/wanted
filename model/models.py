from sqlalchemy import Column, Integer, String, CHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Company(Base):
    __tablename__ = "company"

    idx = Column(Integer, primary_key= True, index=True)
    name_ko = Column(String(50))
    name_en = Column(String(50))
    name_ja = Column(String(50))
    name_tw = Column(String(50))
    tag_ko = Column(String(255))
    tag_en = Column(String(255))
    tag_ja = Column(String(255))
    tag_tw = Column(String(255))
