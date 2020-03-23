from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Case(Base):
    __tablename__ = 'case'
    id = Column(Integer, primary_key=True)
    number = Column(String(60),unique=True)
    date = Column(DateTime, default=datetime.now())
    block = Column(String(60))
    description = Column(String(60))
    location_description = Column(String(60))
    arrest = Column(Boolean)
    domestic = Column(Boolean)
    ivcr_id = Column(Integer,ForeignKey('ivcr.id'))
    crimetype_id = Column(Integer,ForeignKey('CrimeType.id'))
    beat_id = Column(Integer,ForeignKey('beat.id'))
    district_id = Column(Integer,ForeignKey('district.id'))
    ward_id = Column(Integer,ForeignKey('ward.id'))
    communityarea_id = Column(Integer,ForeignKey('CommunityArea.id'))
    fbicode_id = Column(Integer,ForeignKey('FBICode.id'))

    def __repr__(self):
        return self.number


class Ivcr(Base):
    __tablename__ = 'ivcr'
    id = Column(Integer, primary_key=True)
    code = Column(String(32),unique=True)
    cases = relationship('Case', backref='ivcr')

    def __repr__(self):
        return self.code


class CrimeType(Base):
    __tablename__ = 'CrimeType'
    id = Column(Integer, primary_key=True)
    type = Column(String(60),unique=True)
    cases = relationship('Case', backref='crimetype')

    def __repr__(self):
        return self.type


class Beat(Base):
    __tablename__ = 'beat'
    id = Column(Integer, primary_key=True)
    code = Column(String(32),unique=True)
    cases = relationship('Case',backref='beat')

    def __repr__(self):
        self.code

class District(Base):
    __tablename__ = 'district'
    id = Column(Integer, primary_key=True)
    code = Column(String(32),unique=True)
    cases = relationship('Case',backref='district')

    def __repr__(self):
        return self.code


class Ward(Base):
    __tablename__ = 'ward'
    id = Column(Integer, primary_key=True)
    code = Column(String(32),unique=True)
    cases = relationship('Case',backref='ward')

    def __repr__(self):
        return self.id

class CommunityArea(Base):
    __tablename__ = 'CommunityArea'
    id = Column(Integer, primary_key=True)
    code = Column(String(32),unique=True)
    cases = relationship('Case',backref='communityarea')

    def __repr__(self):
        return self.id

class FBICode(Base):
    __tablename__ = 'FBICode'
    id = Column(Integer, primary_key=True)
    code = Column(String(32),unique=True)
    cases = relationship('Case',backref='fbicode')

    def __repr__(self):
        return self.code
