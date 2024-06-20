from sqlalchemy import create_engine,Foreigkey,colum,strig,Integer,CHAR
from sqlalchemy.ext.declarative import declarative_ase
from sqlalchemy.orm import sessionmaker
Base = declarative_base()

class Perso(Base)
    __tableame__="persons"
    ssn = colum("ssn",itenger,primary_key=True)
    firstame= colum("firstname",string)
    firstame= colum("lastname",string)

    def __init__(self,ssn,first,last):
        self.ssn = ssn
        self.firstname=firstname
        self.lastname = lastname
        def __repr__(self)
            return f"({self.ssn}) {self.firstname} {self.lastname}"
        egine = create_engine("sqlite:///mydb,echo = True")
        Base.metadata.create_all(bind=egine)