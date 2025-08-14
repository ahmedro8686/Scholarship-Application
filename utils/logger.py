from loguru import logger
from config import Config
import sys

def init_logger(app=None):
    logger.remove()
    logger.add(sys.stdout, level="INFO")
    logger.add(Config.LOG_FILE, rotation="10 MB", retention="10 days", level="INFO", backtrace=True, diagnose=True)
    
    if app:
        app.logger = logger
