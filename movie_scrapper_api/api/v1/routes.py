from fastapi import APIRouter

from movie_scrapper_api.models.media import MediaModel, SearchModel
from movie_scrapper_api.scrapper import Scrapper

v1_router = APIRouter()


@v1_router.get("/media/{media_name}")
async def get_media_by_name(media_name: str) -> MediaModel:
    scrapper = Scrapper()
    return await scrapper.find_media_by_name(media_name)


@v1_router.get("/search/media/{media_name}")
async def search_media_by_name(media_name: str) -> SearchModel:
    scrapper = Scrapper()
    return await scrapper.search_media(media_name)
