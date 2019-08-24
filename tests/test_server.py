class TestServer():
    @staticmethod
    def test_ping(test_client):
        response = test_client.get('/ping')
        assert response.status_code == 200
        assert b'pong' in response.data

    # TODO need to mock db to be able to run tests below
    # def test_get_users(self):
    #     res = self.app.get('/users')
    #     self.assertEqual(res.status_code, 200)
    #     self.assertIn('Hello World!', str(res.data))

    # def test_post_users(self):
    #     res = self.app.post('/users', data=dict(name='John Doe'))
    #     self.assertEqual(res.status_code, 200)
    #     self.assertIn('success', str(res.data))

    # def test_get_users_after_post(self):
    #     res = self.app.get('/users')
    #     self.assertEqual(res.status_code, 200)
    #     self.assertIn('John Doe', str(res.data))
