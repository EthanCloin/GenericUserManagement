from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

USER = load_dotenv("ROOT_USER")
PASSWORD = load_dotenv("ROOT_PASSWORD")
DB_NAME = load_dotenv("DATABASE_NAME")
HOST = "localhost"

engine = create_engine(f"mysql+mysqldb://{USER}:{PASSWORD}@{HOST}/{DB_NAME}")
Session = sessionmaker(bind=engine)
Base = declarative_base()
