class TestServer():
    @staticmethod
    def test_ping(test_client):
        response = test_client.get('/ping')
        assert response.status_code == 200
        assert b'pong' in response.data

    def test_get_users(self, test_client):
        response = test_client.get('/users')
        assert response.status_code == 200
        assert response.json['status'] == 'success'
        assert response.json['payload'] == []

    # def test_post_user(self, test_client):
    #     response = test_client.post('/users', data=dict(name='John Doe'))
    #     assert response.status_code == 200
    #     assert response.json['status'] == 'success'
    #     assert response.json['payload'] == []

    def test_get_users_after_post(self, test_client):
        response = test_client.get('/users')
        assert response.status_code == 200
        assert response.json['status'] == 'success'
        assert response.json['payload'] == ['John Doe']
