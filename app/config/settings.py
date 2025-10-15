# app/config/settings.py
import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Supply Chain Backend"
    DEBUG: bool = True
    SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecretkey")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    DATABASE_URL: str = os.getenv(
        "DATABASE_URL", "postgresql+asyncpg://user:password@localhost:5432/supply_chain"
    )

    KAFKA_BROKER: str = os.getenv("KAFKA_BROKER", "localhost:9092")
    MQTT_BROKER: str = os.getenv("MQTT_BROKER", "mqtt://localhost:1883")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
