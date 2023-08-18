# Movie Scrapper API

An API written with Python that uses the [OMDB API](http://www.omdbapi.com/) to
scrape data for movies and TV Shows.

## Requirements

- Python (3.10 and newer)
- Poetry

## How to install

```shell
apt-get update -y
apt-get upgrade -y
apt-get install -y python3 python3-pip

pip install poetry
poetry install
poetry self add poetry-dotenv-plugin
```

After installing, create an `.env` file on the root of the project and add your OMDB API key.

Example:
```text
OMDB_API_KEY="YOUR_KEY_HERE"
```

## How to run

```shell
poetry run python -m movie_scrapper_api
```

### Documentation endpoints

* `/docs` -> The docs for the documentation with interactive calls
* `/redoc` -> Alternative docs without interactive calls
