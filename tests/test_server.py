from unittest.mock import patch


class TestServer():
    @staticmethod
    def test_ping(test_client):
        response = test_client.get('/ping')
        assert response.status_code == 200
        assert b'pong' in response.data

    def test_get_users(self, test_client, test_get_db):
        with patch('src.server.get_db', test_get_db):
            response = test_client.get('/users')
        assert response.status_code == 200
        assert response.json['status'] == 'success'
        assert response.json['payload'] == []

    def test_post_user(self, test_client, test_get_db):
        with patch('src.server.get_db', test_get_db):
            response = test_client.post('/users', data=dict(name='John Doe'))
        assert response.status_code == 200
        assert response.json['status'] == 'success'
        assert len(response.json['payload']) == 24

        with patch('src.server.get_db', test_get_db):
            response = test_client.get('/users')
        assert response.status_code == 200
        assert response.json['status'] == 'success'
        assert response.json['payload'] == ['John Doe']

    def test_post_user_missing_data(self, test_client, test_get_db):
        with patch('src.server.get_db', test_get_db):
            response = test_client.post('/users')
        assert response.status_code == 400
        assert response.json['status'] == 'failed'
        assert response.json['payload'] == 'Please insert a name'

    def test_post_user_db_exception(self, test_client, test_get_db):
        with patch('src.server.get_db', side_effect=Exception):
            response = test_client.post('/users', data=dict(name='John Doe'))
        assert response.status_code == 500
        assert response.json['status'] == 'failed'
        assert response.json['payload'] == 'An internal server error happened. Please try again later'
