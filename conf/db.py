import os
import pathlib
import configparser

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# loading variables from .env file
load_dotenv() 

file_config = pathlib.Path(__file__).parent.parent.joinpath("config.ini")
# print(file_config)
config = configparser.ConfigParser()
config.read(file_config)
# test = config.read(file_config)
# print(type(test))


user = config.get("DEV_DB", "USER")
password = config.get("DEV_DB", "PASSWORD")
domain = config.get("DEV_DB", "DOMAIN")
port = config.get("DEV_DB", "PORT")
db = config.get("DEV_DB", "DB_NAME")

URI = f"postgresql://{user}:{password}@{domain}:{port}/{db}"
# print(URI)

DATABASE_URL2 = os.getenv('DATABASE_URL2')

engine = create_engine(DATABASE_URL2, echo=True, pool_size=5, max_overflow=0)
# engine = create_engine(URI, echo=True, pool_size=5, max_overflow=0)
DBSession = sessionmaker(bind=engine)
session = DBSession()
