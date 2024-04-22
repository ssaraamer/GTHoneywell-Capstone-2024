import os
from dotenv import load_dotenv

from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME:str = "Honeywell Chatbot"
    PROJECT_VERSION: str = "1.0.0"

    POSTGRES_USER : str = os.getenv("POSTGRES_USER") #This is the postgres username
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD") #This is the postgres password
    POSTGRES_SERVER : str = os.getenv("POSTGRES_SERVER","localhost") #This is the postgres server default should be localhost
    POSTGRES_PORT : str = os.getenv("POSTGRES_PORT",5432) # default postgres port is 5432, this is how you connect to postgres through UI
    POSTGRES_DB : str = os.getenv("POSTGRES_DB","tdd")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}" # this allows for dynamic changing of usernames and such

#The settings may need to be changed to allow for connections from peoplewho do not have postgresql in their local machine
settings = Settings()