# -*- coding:utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

engine = create_engine('mysql+mysqldb://root@localhost:3306/shiyanlougithub?charset=utf8')
Base = declarative_base()


class Repositories(Base):
    __tablename__ = 'repositories'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), index=True)
    update_time = Column(DateTime)
    commits = Column(String(64), index=True)
    branches = Column(String(64), index=True)
    releases = Column(String(64), index=True)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
