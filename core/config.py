import logging

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict


def is_dev(dev=False):
    if not dev:
        print("ENV")
        load_dotenv()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='../.env', env_file_encoding='utf-8')
    PG_DSN: str = f"postgresql+psycopg://postgres:postgres@localhost:5432/cards"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_HOURS: int = 24 * 15
    TOKEN_SECRET_KEY: str = "abracadabra"
    BROKER_URI: str = "redis://localhost:6379/0"
    SESSION_STORAGE_URI: str = "redis://localhost:6379/1"


settings = Settings()

logger = logging.getLogger()
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))
logger.addHandler(console_handler)
