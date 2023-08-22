from typing import Annotated

from fastapi import APIRouter, HTTPException, Query

from movie_scrapper_api.models.errors import HTTPError
from movie_scrapper_api.models.media import MediaModel, SearchModel, GetMediaMode, MediaType, PlotType
from movie_scrapper_api.scrapper import Scrapper

v1_router = APIRouter()


@v1_router.get(
    "/media",
    status_code=200,
    summary="The info of the media that matches the name given",
    response_description="The media.",
    responses={
        404: {"description": "A media with this name was not found.", "model": HTTPError},
        500: {"description": "A server error has occurred."}
    },
    tags=["Media"]
)
async def get_media(
        q: Annotated[str, Query()],
        mode: Annotated[GetMediaMode, Query()] = GetMediaMode.ID,
        type: Annotated[MediaType | None, Query()] = None,
        year: Annotated[str | None, Query()] = None,
        plot: Annotated[PlotType, Query()] = PlotType.Short
) -> MediaModel:
    scrapper = Scrapper()
    try:
        params = {
            mode.value: q,
            'plot': plot
        }
        if type is not None: params['type'] = type.value
        if year is not None: params['year'] = year
        media = await scrapper.find_media(params)
    except ValueError as err:
        raise HTTPException(status_code=404, detail=str(err))
    return media


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
    try:
        media = await scrapper.search_media(media_name)
    except ValueError as err:
        raise HTTPException(status_code=404, detail=str(err))
    return media
