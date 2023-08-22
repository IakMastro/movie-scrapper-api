import httpx
import pytest

from movie_scrapper_api.scrapper import Scrapper


@pytest.mark.scrapper
@pytest.mark.asyncio
class TestScrapper:
    @pytest.mark.parametrize('params', [
        {
            't': 'asddsadsa'
        },
    ])
    async def test_find_movie_by_wrong_params(self, params):
        scrapper = Scrapper()
        with pytest.raises(ValueError):
            await scrapper.find_media(params)

    @pytest.mark.parametrize("params", [
        {
            't': "The Godfather",
            'type': 'movie'
        },
        {
            "i": "tt0436992",
            "plot": "full"
        }
    ])
    async def test_find_media(self, params):
        scrapper = Scrapper()
        media_data = await scrapper.find_media(params)

        if 't' in params:
            assert media_data.title == params['t']
        else:
            assert media_data.imdb.id == params['i']

    @pytest.mark.parametrize('fake_movie_name', [
        'asddsadsa'
    ])
    async def test_find_movie_by_fake_name(self, fake_movie_name):
        scrapper = Scrapper()
        with pytest.raises(ValueError):
            await scrapper.search_media(fake_movie_name)

    @pytest.mark.parametrize("movie_name", [
        'Doctor Who',
        'The Godfather',
        'Blackadder',
        'Mr. Bean'
    ])
    async def test_search_movie(self, movie_name):
        scrapper = Scrapper()
        media_data = await scrapper.search_media(movie_name)
        assert len(media_data.search) > 0


@pytest.mark.scrapper
@pytest.mark.asyncio
class TestScrapperRouter:
    base_url = "http://localhost:9101/api/v1"

    @pytest.mark.parametrize('params', [
        {
            'q': 'asdsadsada',
            'mode': 't'
        }
    ])
    async def test_get_media_invalid_name(self, params):
        async with httpx.AsyncClient(base_url=self.base_url) as client:
            res = await client.get(
                "/media",
                params=params
            )

        assert res.status_code == 404
        assert res.json()['detail'] == 'Movie not found!'

    @pytest.mark.parametrize("params", [
        {
            'q': "The Godfather",
            'mode': 't',
            'type': 'movie'
        },
        {
            "q": "tt0436992",
            'mode': 'i',
            "plot": "full"
        }
    ])
    async def test_get_media(self, params):
        async with httpx.AsyncClient(base_url=self.base_url) as client:
            res = await client.get(
                "/media",
                params=params
            )

        assert res.status_code == 200
        if params['mode'] == 't':
            assert res.json()['title'] == params['q']
        else:
            assert res.json()['imdb']['id'] == params['q']

    @pytest.mark.parametrize('fake_movie_name', [
        'asddsadsa'
    ])
    async def test_get_movie_wrong_name(self, fake_movie_name):
        async with httpx.AsyncClient(base_url=self.base_url) as client:
            res = await client.get(f"/search/media/{fake_movie_name}")

        assert res.status_code == 404
        assert res.json()['detail'] == 'Movie not found!'

    @pytest.mark.parametrize("movie_name", [
        'Doctor Who',
        'The Godfather',
        'Blackadder',
        'Mr. Bean'
    ])
    async def test_search_movie(self, movie_name):
        async with httpx.AsyncClient(base_url=self.base_url) as client:
            res = await client.get(f"/search/media/{movie_name}")

        assert res.status_code == 200
        assert len(res.json()['search']) > 0
