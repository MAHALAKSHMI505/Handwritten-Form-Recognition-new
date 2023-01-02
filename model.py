from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from flask import *
from sqlalchemy import *

Base = declarative_base()
engine = create_engine('sqlite:///user.db',connect_args={'check_same_thread': False})
engine.connect()
Session = sessionmaker(bind=engine)
sqlsession = Session()


class User(Base):
    __tablename__ = "user"

    id = Column('id', Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column('name', String(255))
    emailid = Column('emailid', String(255))
    username = Column('username', String(255))
    password = Column('password', String(255))
    templates = relationship('TemplateData', backref = 'user', cascade="save-update, merge, delete")
    fields = relationship('Field', backref = 'user', cascade="save-update, merge, delete")
    originaltable = relationship('OriginalTable', backref = 'user', cascade="save-update, merge, delete")
    modifiedtables = relationship('ModifiedTables', backref = 'user', cascade="save-update, merge, delete")


class TemplateData(Base):
    __tablename__ = "templatedata"

    id = Column('id', Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column('name', String(255))
    description = Column('description', String(9999999999))
    imagelink = Column('imagelink', String(999999999999))
    csvlink = Column('csvlink', String(999999999999))
    formtype = Column('formtype', String(999999))
    language = Column('language', String(999999))
    createdon = Column('createdon', String(9999999999))
    userid = Column('userid', Integer, ForeignKey('user.id'))
    fields = relationship('Field',backref = 'templatedata', cascade="save-update, merge, delete")
    originaltable = relationship('OriginalTable',backref = 'templatedata', cascade="save-update, merge, delete")
    modifiedtables = relationship('ModifiedTables',backref = 'templatedata', cascade="save-update, merge, delete")

class Field(Base):
    __tablename__ = 'field'

    id = Column('id', Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column('name', String(255))
    Type = Column('type', String(255))
    description = Column('description', String(25555))
    leftx = Column('leftx', Integer)
    rightx = Column('rightx', Integer)
    topy = Column('topy', Integer)
    bottomy = Column('bottomy', Integer)
    percentleftx = Column('percentleftx', Float)
    percentrightx = Column('percentrightx', Float)
    percenttopy = Column('percenttopy', Float)
    percentbottomy = Column('percentbottomy', Float)
    templateid = Column('templateid',Integer, ForeignKey('templatedata.id'))
    userid = Column('userid', Integer, ForeignKey('user.id'))
    markedon = Column('markedon', String(255))
    anchor = Column('anchor', Boolean)

class OriginalTable(Base):
    __tablename__ = "originaltable"

    id = Column('id', Integer, Sequence('user_id_seq'), primary_key=True)
    rid=Column('rid',Integer)
    ChildId = Column('ChildId', JSON)
    ChildFirstName = Column('ChildFirstName', JSON)
    ChildLastName = Column('ChildLastName', JSON)
    MothersFirstName = Column('MothersFirstName', JSON)
    MothersLastName = Column('MothersLastName', JSON)
    FathersFirstName = Column('FathersFirstName', JSON)
    FathersLastName = Column('FathersLastName', JSON)
    ChildsAadharId = Column('ChildsAadharId', JSON)
    DateofBirth = Column('DateofBirth', JSON)
    Caste = Column('Caste', JSON)
    Religion = Column('Religion', JSON)
    Sex = Column('Sex',JSON)
    Yearoffirstlisting = Column('Yearoffirstlisting', JSON)
    Monthandyearlastupdated = Column('Monthandyearlastupdated', JSON)
    TypeofDisability = Column('TypeofDisability', JSON)
    Resident = Column('Resident', JSON)
    MonthandYearofInMigration = Column('MonthandYearofInMigration', JSON)
    ICDSServicesforPSE = Column('ICDSServicesforPSE', JSON)
    ICDSServicesforSNP = Column('ICDSServicesforSNP', JSON)
    userid = Column('userid', Integer, ForeignKey('user.id'))
    templateid = Column('templateid',Integer, ForeignKey('templatedata.id'))

class ModifiedTables(Base):
    __tablename__ = "modifiedtables"

    id = Column('id', Integer, Sequence('user_id_seq'), primary_key=True)
    rid=Column('rid',Integer)
    ChildId = Column('ChildId', JSON)
    ChildFirstName = Column('ChildFirstName', JSON)
    ChildLastName = Column('ChildLastName', JSON)
    MothersFirstName = Column('MothersFirstName', JSON)
    MothersLastName = Column('MothersLastName', JSON)
    FathersFirstName = Column('FathersFirstName', JSON)
    FathersLastName = Column('FathersLastName', JSON)
    ChildsAadharId = Column('ChildsAadharId', JSON)
    DateofBirth = Column('DateofBirth', JSON)
    Caste = Column('Caste', JSON)
    Religion = Column('Religion', JSON)
    Sex = Column('Sex',JSON)
    Yearoffirstlisting = Column('Yearoffirstlisting', JSON)
    Monthandyearlastupdated = Column('Monthandyearlastupdated', JSON)
    TypeofDisability = Column('TypeofDisability', JSON)
    Resident = Column('Resident', JSON)
    MonthandYearofInMigration = Column('MonthandYearofInMigration', JSON)
    ICDSServicesforPSE = Column('ICDSServicesforPSE', JSON)
    ICDSServicesforSNP = Column('ICDSServicesforSNP', JSON)
    userid = Column('userid', Integer, ForeignKey('user.id'))
    templateid = Column('templateid',Integer, ForeignKey('templatedata.id'))
    
    

Base.metadata.create_all(bind=engine)
