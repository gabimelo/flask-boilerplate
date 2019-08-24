import pytest
from pymongo import MongoClient

from src.server import app


def test_get_db_internal():
    client = MongoClient('mongodb://db:27017/')
    db = client.test_database
    return db


@pytest.fixture(scope='module')
def test_get_db():
    client = MongoClient('mongodb://db:27017/')
    db = client.test_database
    db.users.delete_many({})
    yield test_get_db_internal


@pytest.fixture(scope='module')
def test_client():
    app.testing = True
    return app.test_client()
