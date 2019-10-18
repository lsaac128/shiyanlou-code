from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


engine = create_engine('mysql+mysqldb://root@localhost:3306/wangliang?charset=utf8')
Base = declarative_base()



class Wang(Base):
    __tablename__ = 'wang'
    id = Column(Integer, primary_key=True)
    title = Column(String(64))
    name = Column(String(64))


if __name__ == '__main__':
    Base.metadata.create_all(engine)
