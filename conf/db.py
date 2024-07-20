import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# loading variables from .env file
load_dotenv() 

DATABASE_URL2 = os.getenv('DATABASE_URL2')

engine = create_engine(DATABASE_URL2, echo=False, pool_size=5, max_overflow=0)
DBSession = sessionmaker(bind=engine)
session = DBSession()
