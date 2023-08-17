import pytest

from movie_scrapper_api.scrapper import Scrapper


@pytest.mark.scrapper
@pytest.mark.asyncio
class TestScrapper:
    @pytest.mark.parametrize('fake_movie_name', [
        'asddsadsa'
    ])
    async def test_find_movie_by_fake_name(self, fake_movie_name):
        scrapper = Scrapper()
        with pytest.raises(ValueError) as err:
            await scrapper.find_media_by_name(fake_movie_name)
            assert err == "Movie with this name is not found!"

    @pytest.mark.parametrize('movie_name', [
        'Doctor Who',
        'The Godfather',
        'Blackadder',
        'Mr. Bean'
    ])
    async def test_find_movie_by_name(self, movie_name):
        scrapper = Scrapper()
        movie_data = await scrapper.find_media_by_name(movie_name)
        assert movie_data.title == movie_name

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
