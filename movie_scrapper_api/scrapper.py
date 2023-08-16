import httpx

from movie_scrapper_api.config import settings
from movie_scrapper_api.models.media import MediaModel, Rating, SearchModel


class Scrapper:
    __client: httpx.AsyncClient

    def __init__(self):
        self.__client = httpx.AsyncClient(
            base_url="https://omdbapi.com"
        )

    async def find_media_by_name(self, media_name) -> MediaModel:
        response = await self.__client.get(
            "",
            params={
                "apikey": settings.OMDB_API_KEY,
                "plot": "full",
                "t": media_name
            }
        )

        media_data = response.json()
        if "Error" in media_data:
            raise ValueError(media_data['Error'])

        ratings = []
        for rating in media_data['Ratings']:
            ratings.append(
                {
                    'source': rating['Source'],
                    'value': rating['Value']
                }
            )

        return MediaModel.parse_obj({
            'title': media_data['Title'],
            'year': media_data['Year'],
            'rated': media_data['Rated'],
            'released': media_data['Released'],
            'runtime': media_data['Runtime'],
            'genres': media_data['Genre'].split(','),
            'director': media_data['Director'],
            'writers': media_data['Writer'].split(','),
            'actors': media_data['Actors'].split(','),
            'plot': media_data['Plot'],
            'languages': media_data['Language'].split(','),
            'country': media_data['Country'],
            'awards': media_data['Awards'],
            'poster': media_data['Poster'],
            'ratings': ratings,
            'imdb': {
                'rating': media_data['imdbRating'],
                'votes': media_data['imdbVotes'],
                'id': media_data['imdbID']
            },
            'type': media_data['Type'],
            'embed': f"https://vidsrc.to/embed/{media_data['Type']}/{media_data['imdbID']}"
        })

    async def search_media(self, media_name: str) -> SearchModel:
        response = await self.__client.get(
            "",
            params={
                "apikey": settings.OMDB_API_KEY,
                "s": media_name
            }
        )

        media_data = response.json()
        search_data = []
        for media in media_data['Search']:
            search_data.append({
                "title": media['Title'],
                "year": media["Year"],
                "imdbID": media["imdbID"],
                "type": media["Type"],
                "poster": media["Poster"]
            })
        return SearchModel.parse_obj({
            "search": search_data
        })
