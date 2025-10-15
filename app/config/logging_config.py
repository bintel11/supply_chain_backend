# app/config/logging_config.py
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("supply_chain_backend")
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

file_handler = RotatingFileHandler("logs/app.log", maxBytes=5*1024*1024, backupCount=3)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
