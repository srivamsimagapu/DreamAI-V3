
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column,Integer,String,Text
Base=declarative_base()
class Dream(Base):
    __tablename__='dreams'
    id=Column(Integer,primary_key=True)
    title=Column(String(200))
    content=Column(Text)
