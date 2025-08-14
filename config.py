import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///scholarshiphub.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SCRAPER_DELAY = int(os.getenv("SCRAPER_DELAY", 2))  # seconds between requests
    LOG_FILE = os.getenv("LOG_FILE", "logs/app.log")
    ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "admin@scholarshiphub.com")
