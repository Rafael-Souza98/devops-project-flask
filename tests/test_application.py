from sqlite3 import connect
import warnings
import pytest
from application import create_app
import mongomock


class TestApplication():

    @pytest.fixture
    def client(self):
        app  = create_app('config.MockConfig')
        return app.test_client()

    @pytest.fixture
    def valid_user(self):
        return { 
                "first_name": "rafael",
                "last_name": "souza",
                "cpf": "440.513.740-41",
                "email": "faelsos98@gmail.com",
                "birthday_date": "1998-02-12"
                }
    @pytest.fixture
    def invalid_user(self):
        return { 
                "first_name": "rafael",
                "last_name": "souza",
                "cpf": "440.513.740-21",
                "email": "faelsos98@gmail.com",
                "birthday_date": "1998-02-12"
                }

    def test_get_users(self, client):
        resp = client.get('/user')
        assert resp.status_code == 200
    
    def test_post_user(self, client, valid_user, invalid_user):
        resp = client.post('/user', json=valid_user)
        assert resp.status_code == 200
        assert b"successfully" in resp.data

        resp = client.post('/user', json=invalid_user)
        assert resp.status_code == 400
        assert b"invalid" in resp.data
    
    def test_get_user_by_cpf(self, client, valid_user, invalid_user):
        resp = client.get('/user/%s' % valid_user['cpf'] )
        assert resp.status_code == 200
        assert resp.json[0]["first_name"] == "rafael"
        assert resp.json[0]["last_name"] == "souza"
        assert resp.json[0]["cpf"] == "440.513.740-41"
        assert resp.json[0]["birthday_date"]["$date"] == '1998-02-12T00:00:00Z'

        resp = client.get('/user/%s' % invalid_user['cpf'] )
        assert resp.status_code == 400
        assert b"User doesn't exist" in resp.data
        