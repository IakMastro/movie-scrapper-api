from pathlib import Path

from fastapi import FastAPI

from movie_scrapper_api.config import setup_app_logging, settings

BASE_PATH = Path(__file__).resolve().parent

setup_app_logging(config=settings)
app = FastAPI(
    title="Movie Scrapper API",
    swagger_ui_parameters={
        "syntaxHighlight.theme": "monokai"
    },
)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        app,
        host=settings.BIND_HOST,
        port=settings.BIND_PORT,
        log_level=settings.LOG_LEVEL,
    )
