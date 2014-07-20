#!/usr/bin/env python
# -*- coding:utf-8 -*-
# *******************************************************************
# Author: Ioannis Pinakoulakis
# Created: Tue Nov 25 00:11:10 2014 (+0100)
# Description:
# *******************************************************************
# TODO:
# 1) verify the basic model, test it on MySQL.§
# 2) add code to generate the new tables
# *******************************************************************
#
from sqlalchemy import (Column, Integer, DateTime, ForeignKey,
                        select, String, Table)
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.rom import relationship
from sqlalchemy.schema import CreateTable

Base = declarative_base()

class TableName(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__Name__.lower()

class UTF8TableName(object):
    @declared_attr
    def mysql_charset(cls):
        return 'utf-8'

class Provider(TableName, Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(150))

class Keywords(TableName, Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(80))

# many-to-many connection between tags and news
news_tags = Table('news_keywords', Base.metadata,
                  Column('news_id', Integer, ForeignKey('news.id')),
                  Column('keywords_id', Integer, ForeignKey('keywords.id'))
)

class News(TableName, Base):
    id = Column(Integer, primary_key=True)
    hash_id = Column(String(256))
    link = Column(String(2048))
    title = Column(String(150))
    description = Column(String(250))
    contents = Column(String(10000))
    date_added = Column(DateTime)
    language = Column(String(5))
    author = Column(String(100))

    provider_id = Column(Integer, ForeignKey('provide.id'))
    provider = relationship('Provider', backref='provider')
    
    keywords = relationship('Keywords', secondary=news_keywords)

