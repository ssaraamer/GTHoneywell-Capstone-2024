from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import settings


SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
print("Database URL is ",SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#This line starts the FastAPI server which connects through sqlalchemy to the postgresql database
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
