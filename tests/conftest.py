import pytest
from unittest.mock import patch
from pymongo import MongoClient


@pytest.fixture(scope='module')
def test_mongo():
    client = MongoClient('mongodb://db:27017/')
    db = client.test_database
    db.users.delete_many({})
    return db


@pytest.fixture(scope='module')
def test_client(test_mongo):
    with patch('src.server.db', test_mongo):
        from src.server import app
        app.testing = True
    return app.test_client()
