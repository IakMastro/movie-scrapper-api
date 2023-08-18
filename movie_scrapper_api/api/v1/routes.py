from fastapi import APIRouter

from movie_scrapper_api.models.errors import HTTPError
from movie_scrapper_api.models.media import MediaModel, SearchModel
from movie_scrapper_api.scrapper import Scrapper

v1_router = APIRouter()


@v1_router.get(
    "/media/{media_name}",
    status_code=200,
    summary="The info of the media that matches the name given",
    response_description="The media.",
    responses={
        404: {"description": "A media with this name was not found.", "model": HTTPError},
        500: {"description": "A server error has occurred."}
    },
    tags=["Media"]
)
async def get_media_by_name(media_name: str) -> MediaModel:
    scrapper = Scrapper()
    return await scrapper.find_media_by_name(media_name)


@v1_router.get(
    "/search/media/{media_name}",
    status_code=200,
    summary="A list media that matches the name given",
    response_description="A list of media.",
    responses={
        404: {"description": "A media with this name was not found.", "model": HTTPError},
        500: {"description": "A server error has occurred."}
    },
    tags=["Media", "Search"]
)
async def search_media_by_name(media_name: str) -> SearchModel:
    scrapper = Scrapper()
    return await scrapper.search_media(media_name)
