from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, HttpUrl, Field, model_validator


class Rating(BaseModel):
    """
    The rating of the media.

    Fields:

    - **source**: Of type `str`
    - **version**: Of type `str`
    """
    source: str = Field(
        title="The Rating's source",
        example="Internet Movie Database",
        description="The source of the rating"
    )
    value: str = Field(
        title="The Rating's value",
        example="8.6/10",
        description="The value of the rating"
    )


class IMDB(BaseModel):
    """
    IMDB info of the media.

    Fields:
    - **rating**: Of type `float`.
    - **votes**: Of type `float`.
    - **id**: Of type `str`.
    """
    rating: str = Field(
        title="IMDB Rating",
        example="8.6",
        description="The rating in IMDB"
    )
    votes: str = Field(
        title="IMDB Votes",
        example="232.909",
        description="The number of the votes in IMDB"
    )
    id: str = Field(
        title="IMDB ID",
        example="tt0436992",
        description="The ID of the media in IMDB"
    )


class MediaType(str, Enum):
    """The type of the media"""
    Movie = "movie"
    TvShow = "series"
    Episode = "episode"
    Game = "game"


class MediaModel(BaseModel):
    """
    The Media object.

    Fields:

    - **title**: The title of the media.
    - **year**: The year the media was released.
    - **rated**: The parental rating of the media.
    - **genres**: A list of the genres the media belongs to.
    - **director**: The director of the media. In case of multiple, the main one.
    - **writers**: The writers of the media.
    - **actors**: The actors of the media.
    - **plot**: The plot of the media's story.
    - **languages**: The featured languages spoken in the media.
    - **country**: The origin of the media's country.
    - **awards**: A brief summary of the media's awards (if any).
    - **poster**: A URL of the poster.
    - **imdb**: The IMDB page of the media. It is of type `IMDB`.
    - **type**: The type of the media. It is of type `MediaType`.
    - **embed**: The URL of the embed of the media.
    """
    title: str = Field(
        title="The Title of the Media",
        example="Doctor Who",
        description="The official title of the media"
    )
    year: str = Field(
        title="The Year",
        example="2005-",
        description="The year the media came out"
    )
    rated: str = Field(
        title="The Rating of the Media",
        example="TV-PG",
        description="The official parental rating of the media"
    )
    released: str = Field(
        title="The Release Date of the Media",
        example="17 Mar 2006",
        description="The initial release date of the media"
    )
    genres: List[str] = Field(
        title="The Genres of the Media",
        example=["Adventure", "Drama", "Sci-Fi"],
        description="The genres of the media in a list"
    )
    director: str = Field(
        title="The Director of the Media",
        example="N/A",
        description="The director of the media. In case of many, the primary one will be listed."
    )
    writers: List[str] = Field(
        title="The Writers of the Media",
        example=["Sydney Newman"],
        description="The writers of the media in a list"
    )
    actors: List[str] = Field(
        title="The Actors of the Media",
        example=["Jodie Whittaker", "Peter Capaldi", "Pearl Mackie"],
        description="The main cast of the media"
    )
    plot: str = Field(
        title="The Plot of the Media",
        example="The Doctor, a Time Lord from the race whose home planet is Gallifrey, travels through time and "
                "space in their ship the TARDIS (an acronym for Time and Relative Dimension In Space) with numerous "
                "companions. From time to time, the Doctor regenerates into a new form.",
        description="The full plot of the media"
    )
    languages: List[str] = Field(
        title="The Languages of the Media",
        examples=["English"],
        description="The languages spoken in the media"
    )
    countries: List[str] = Field(
        title="The Countries of Origin",
        examples=["United Kingdom", "United States"],
        description="The countries of origin of the media in a list"
    )
    awards: str = Field(
        title="The Awards of the Media",
        example="Won 4 BAFTA 119 wins & 219 nominations total",
        description="The awards of the media"
    )
    poster: HttpUrl = Field(
        title="The Post of the Media",
        example="https://m.media-amazon.com/images/M/MV5B"
                "ZWJhYjFmZDEtNTVlYy00NGExLWJhZWItNTAxODY5YTc3MDFmXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_SX300.jpg",
        description="The URL of the poster"
    )
    ratings: List[Rating] = Field(
        title="The Ratings of the Media",
        example=[
            {
                "source": "Internet Movie Database",
                "value": "8.6/10"
            }
        ],
        description="The ratings of the media through the internet"
    )
    imdb: IMDB = Field(
        title="The IMDB of the Media",
        example={
            "rating": "8.6",
            "votes": "232,909",
            "id": "tt0436992"
        },
        description="The IMDB info on the media"
    )
    type: MediaType = Field(
        title="The Type of the Media",
        example="series",
        description="The type of the media."
    )
    embed: HttpUrl = Field(
        title="The Embed of the Media",
        example="https://vidsrc.to/embed/series/tt0436992",
        description="The vidsrc URL of the media. DISCLAIMER: Some links may not work as they are not tested"
    )


class PlotType(str, Enum):
    Short = "short"
    Full = "full"


class GetMediaMode(str, Enum):
    ID = "i"
    Title = "t"


class SearchMedia(BaseModel):
    """
    The Search's model.

    Fields:

    - **title**: The title of the media
    - **year**: The year the media was released
    - **imdbID**: The ID given by IMDB
    - **type**: The type of the media. It's of type `MediaType`.
    - **poster**: The URL of the poster.
    """
    title: str = Field(
        title="The Title of the Media",
        example="Doctor Who",
        description="The official title of the media"
    )
    year: str = Field(
        title="The Year",
        example="2005-",
        description="The year the media came out"
    )
    imdbID: str = Field(
        title="The ID from IMDB",
        example="tt0436992",
        description="The ID from the IMDB of the media"
    )
    type: MediaType = Field(
        title="The Type of the Media",
        example="series",
        description="The type of the media."
    )
    poster: Optional[HttpUrl] = Field(
        title="The Post of the Media",
        example="https://m.media-amazon.com/images/M/MV5BZWJhYjFmZDEtNTVlYy0"
                "0NGExLWJhZWItNTAxODY5YTc3MDFmXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_SX300.jpg",
        description="The URL of the poster"
    )


class SearchModel(BaseModel):
    """The return object of `GET /api/v1/search`"""
    search: List[SearchMedia] = Field(
        title="A list of the media that matches the title given",
        example={
            "search": [
                {
                    "title": "The Godfather",
                    "year": "1972",
                    "imdbID": "tt0068646",
                    "type": "movie",
                    "poster": "https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlOD"
                              "Y3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg"
                },
                {
                    "title": "The Godfather Part II",
                    "year": "1974",
                    "imdbID": "tt0071562",
                    "type": "movie",
                    "poster": "https://m.media-amazon.com/images/M/MV5BMWMwMGQzZTItY2JlNC00OWZiLWIyMDctNDk2"
                              "ZDQ2YjRjMWQ0XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg"
                },
                {
                    "title": "The Godfather Part III",
                    "year": "1990",
                    "imdbID": "tt0099674",
                    "type": "movie",
                    "poster": "https://m.media-amazon.com/images/M/MV5BNWFlYWY2YjYtNjdhNi00MzVlLTg2MTMtM"
                              "WExNzg4NmM5NmEzXkEyXkFqcGdeQXVyMDk5Mzc5MQ@@._V1_SX300.jpg"
                },
                {
                    "title": "The Godfather Trilogy: 1901-1980",
                    "year": "1992",
                    "imdbID": "tt0150742",
                    "type": "movie",
                    "poster": "https://m.media-amazon.com/images/M/MV5BMjk5ODZjYmMtYTJjNy00MTU2LWI5OTY"
                              "tYTg5YjFlMDk3ZjI0XkEyXkFqcGdeQXVyODAyNDE3Mw@@._V1_SX300.jpg"
                },
                {
                    "title": "The Godfather Saga",
                    "year": "1977",
                    "imdbID": "tt0809488",
                    "type": "series",
                    "poster": "https://m.media-amazon.com/images/M/MV5BNzk3NmZmMjgtMjA4NS00MjdkLTlkZmM"
                              "tZGFkMDAyNWU4NDdlXkEyXkFqcGdeQXVyODAyNDE3Mw@@._V1_SX300.jpg"
                },
                {
                    "title": "The Godfather",
                    "year": "2006",
                    "imdbID": "tt0442674",
                    "type": "game",
                    "poster": "https://m.media-amazon.com/images/M/MV5BMTQyNTE4NzMzNF5BMl5Ban"
                              "BnXkFtZTgwMDgzNTY3MDE@._V1_SX300.jpg"
                },
                {
                    "title": "The Godfather II",
                    "year": "2009",
                    "imdbID": "tt1198207",
                    "type": "game",
                    "poster": "https://m.media-amazon.com/images/M/MV5BOGMzMTIwMzQtZWExZC00OTZhLWJjNjM"
                              "tYjY4MGY1NzI1ZjMyXkEyXkFqcGdeQXVyOTkwMTc4ODQ@._V1_SX300.jpg"
                },
                {
                    "title": "The Godfather Family: A Look Inside",
                    "year": "1990",
                    "imdbID": "tt0101961",
                    "type": "movie",
                    "poster": "https://m.media-amazon.com/images/M/MV5BZTMyNz"
                              "E0NWEtOGZjYi00ODU0LWE0OTItMzY5YTllYTcyYzgyXkEyXkFqcGdeQXVyODAyNDE3Mw@@._V1_SX300.jpg"
                },
                {
                    "title": "The Godfather Legacy",
                    "year": "2012",
                    "imdbID": "tt2311160",
                    "type": "movie",
                    "poster": "https://m.media-amazon.com/images/M/MV5BNDdmZWViZjgtN2YxMi00OGE4LWI2"
                              "ZjAtNWQwYTJlYjBmZTdhXkEyXkFqcGdeQXVyODAyNDE3Mw@@._V1_SX300.jpg"
                },
                {
                    "title": "Herschell Gordon Lewis: The Godfather of Gore",
                    "year": "2010",
                    "imdbID": "tt1683431",
                    "type": "movie",
                    "poster": "https://m.media-amazon.com/images/M/MV"
                              "5BMTM4NzYzMzgzM15BMl5BanBnXkFtZTgwMDg4NDA2MDE@._V1_SX300.jpg"
                }
            ]
        }
    )
