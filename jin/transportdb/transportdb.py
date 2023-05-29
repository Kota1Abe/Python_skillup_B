from sqlalchemy import create_engine,column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from sqlalchemy.orm import *


DATABASE = "mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8".format(**{
    "user":os.getenv("DB_USER","root"),
    "password":os.getenv("DB_PASSWORD","mysql"),
    "host":os.getenv("DB_HOST","localhost"),
    "database":os.getenv("DB_DATABESE","ENSHU")
})
ENGINE = create_engine(
    DATABASE,
    encoding = "utf-8",
    echo=True 
)
session = scoped_session(
        sessionmaker(
            autocommit =False,
            autoflush =False,
            bind = ENGINE
        )
    )

Base = declarative_base()
Base.query = session.query_property()