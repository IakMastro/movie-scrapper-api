from enum import Enum
from typing import List

from pydantic.v1 import BaseModel, HttpUrl


class Rating(BaseModel):
    source: str
    value: str


class IMDB(BaseModel):
    rating: str
    votes: str
    id: str


class MediaType(str, Enum):
    Movie = "movie"
    TvShow = "series"
    Episode = "episode"


class MediaModel(BaseModel):
    title: str
    year: str
    rated: str
    released: str
    genres: List[str]
    director: str
    writers: List[str]
    actors: List[str]
    plot: str
    languages: List[str]
    country: str
    awards: str
    poster: HttpUrl
    ratings: List[Rating]
    imdb: IMDB
    type: MediaType
    embed: HttpUrl


class SearchMedia(BaseModel):
    title: str
    year: str
    imdbID: str
    type: MediaType
    poster: HttpUrl


class SearchModel(BaseModel):
    search: List[SearchMedia]
