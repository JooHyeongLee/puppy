import os

from pydantic_settings import BaseSettings

class Config(BaseSettings):
    ENV: str = "development"
    DEBUG: str = "1"
    APP_HOST: str = "127.0.0.1"
    APP_PORT: int = 8000
    WRITER_DB_URL: str = f"mysql+aiomysql://user:password@localhost:3306/db"
    READER_DB_URL: str = f"mysql+aiomysql://user:password@localhost:3307/db"

class DevelopmentConfig(Config):
    WRITER_DB_URL: str = f"mysql+aiomysql://user:password@db:3306/db"
    READER_DB_URL: str = f"mysql+aiomysql://user:password@db:3307/db"


class LocalConfig(Config):
    WRITER_DB_URL: str = f"mysql+aiomysql://user:password@localhost:3306/db"
    READER_DB_URL: str = f"mysql+aiomysql://user:password@localhost:3307/db"


class ProductionConfig(Config):
    DEBUG: str = "0"
    WRITER_DB_URL: str = f"mysql+aiomysql://user:password@localhost:3306/db"
    READER_DB_URL: str = f"mysql+aiomysql://user:password@localhost:3306/db"


def get_config():
    env = os.getenv("ENV", "local")
    config_type = {
        "dev": DevelopmentConfig(),
        "local": LocalConfig(),
        "prod": ProductionConfig(),
    }
    return config_type[env]


config: Config = get_config()