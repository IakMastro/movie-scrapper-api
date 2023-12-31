import httpx

from movie_scrapper_api.config import settings
from movie_scrapper_api.models.media import MediaModel, SearchModel


class Scrapper:
    __client: httpx.AsyncClient

    def __init__(self):
        self.__client = httpx.AsyncClient(
            base_url="https://omdbapi.com"
        )

    async def find_media(self, params: dict) -> MediaModel:
        params['apiKey'] = settings.OMDB_API_KEY
        response = await self.__client.get(
            "",
            params=params
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

        return MediaModel.model_validate({
            'title': media_data['Title'],
            'year': media_data['Year'],
            'rated': media_data['Rated'],
            'released': media_data['Released'],
            'runtime': media_data['Runtime'],
            'genres': [genre.strip() for genre in media_data['Genre'].split(',')],
            'director': media_data['Director'],
            'writers': [writer.strip() for writer in media_data['Writer'].split(',')],
            'actors': [actor.strip() for actor in media_data['Actors'].split(',')],
            'plot': media_data['Plot'],
            'languages': [language.strip() for language in media_data['Language'].split(',')],
            'countries': [country.strip() for country in media_data['Country'].split(',')],
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
        if "Error" in media_data:
            raise ValueError(media_data['Error'])

        search_data = []
        for media in media_data['Search']:
            search_data.append({
                "title": media['Title'],
                "year": media["Year"],
                "imdbID": media["imdbID"],
                "type": media["Type"],
                "poster": media["Poster"] if media['Poster'] != "N/A" else None
            })
        return SearchModel.model_validate({
            "search": search_data
        })
