from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from src.definitions.credentials import EnvVariables

DATABASE_URL = EnvVariables.database_url()

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
