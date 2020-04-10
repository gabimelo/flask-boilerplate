import pytest
from pymongo import MongoClient


def _test_get_db():
    client = MongoClient('mongodb://db:27018/')
    db = client.test_database
    return db


@pytest.fixture(scope='module')
def test_get_db():
    client = MongoClient('mongodb://db:27018/')
    db = client.test_database
    db.users.delete_many({})
    yield _test_get_db
