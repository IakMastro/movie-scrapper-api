import importlib.metadata
from pathlib import Path

from fastapi import FastAPI

from movie_scrapper_api.api.v1.routes import v1_router
from movie_scrapper_api.config import setup_app_logging, settings

BASE_PATH = Path(__file__).resolve().parent

description = """
## Movie Scrapper API

Find movies and TV shows fast and easily!

More features are coming out in the future, observe the changelog!
"""

tags_metadata = [
    {
        "name": "Search",
        "description": "Search the IMDB for a specific media"
    },
    {
        "name": "Media",
        "description": "Functions of the media"
    }
]

version = importlib.metadata.version('movie-scrapper-api')

setup_app_logging(config=settings)
app = FastAPI(
    title="Movie Scrapper API",
    description=description,
    version=version,
    openapi_tags=tags_metadata,
    swagger_ui_parameters={
        "syntaxHighlight.theme": "monokai"
    },
)

app.include_router(v1_router, prefix="/api/v1")

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        app,
        host=settings.BIND_HOST,
        port=settings.BIND_PORT,
        log_level=settings.LOG_LEVEL,
    )
