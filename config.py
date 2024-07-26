from dotenv import load_dotenv
from pathlib import Path
import os


env_path = Path(".") / ".env"

load_dotenv(dotenv_path=env_path)

# env vars
class Config:
    DATABASE_URL = os.getenv("DATABASE_URL")
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")

allowed_hosts = ["127.0.0.1"]