from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv


load_dotenv()
USER = os.environ.get("ROOT_USER")
PASSWORD = os.environ.get("ROOT_PASSWORD")
DB_NAME = os.environ.get("DATABASE_NAME")
HOST = "localhost"

print(f"mysql+mysqldb://{USER}:{PASSWORD}@{HOST}/{DB_NAME}")
engine = create_engine(f"mysql+mysqldb://{USER}:{PASSWORD}@{HOST}/{DB_NAME}")
Session = sessionmaker(bind=engine)
Base = declarative_base()
