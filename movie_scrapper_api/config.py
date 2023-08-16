import logging
import sys

from loguru import logger
from pydantic.v1 import BaseSettings

from movie_scrapper_api.logging import InterceptHandler


class Settings(BaseSettings):
    LOG_LEVEL: int = logging.INFO
    BIND_HOST: str = "0.0.0.0"
    BIND_PORT: int = 9101
    OMDB_API_KEY: str


def setup_app_logging(config: Settings) -> None:
    LOGGERS = ("uvicorn.asgi", "uvicorn.access")
    logging.getLogger().handlers = [InterceptHandler()]
    for logger_name in LOGGERS:
        logging_logger = logging.getLogger(logger_name)
        logging_logger.handlers = [InterceptHandler(level=config.LOG_LEVEL)]

    logger.configure(
        handlers=[
            {
                "sink": sys.stderr,
                "level": config.LOG_LEVEL
            }
        ]
    )


settings = Settings()
