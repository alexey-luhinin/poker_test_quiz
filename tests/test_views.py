import pytest
from poker_quiz import app
from services.registration import add_new_user


def login(username, password):
    return app.test_client().post('/login',
                                  data=dict(username=username,
                                            password=password),
                                  follow_redirects=True)


def registration(username, email, password, re_password):
    return app.test_client().post('/registration',
                                  data=dict(username=username,
                                            password=password,
                                            email=email,
                                            re_password=re_password),
                                  follow_redirects=True)


def get_page(URI: str):
    return app.test_client().get(URI, follow_redirects=True)


@pytest.mark.parametrize('username, password, expected',
                         [('admin', '1234', 'Wrong'),
                          ('user1', 'User1User1!', 'Начать')])
def test_login(username, password, expected):
    receive = login(username, password)
    assert expected.encode() in receive.data


@pytest.mark.parametrize('username, password, email,re_password, expected',
                         [('kate', '1234',
                           'kate@gmail.com', '1234', 'Username must'),
                          ('kate1', '1234',
                           'kate@gmail.com', '1234', 'The password'),
                          ('kate1', '1234',
                           'kategmail.com', '1234', 'format of email'),
                          ('kate1', '_3+DaB{h',
                           'kate@gmail.com', 'Y!:5jdq<', 'are not equals')])
def test_registration(username, password, email, re_password, expected):
    receive = registration(username, email, password, re_password)
    assert expected.encode() in receive.data


class TestGetPages:
    def test_get_index_status_code(self):
        assert get_page('/').status_code == 200

    def test_get_test_status_code(self):
        assert get_page('/test').status_code == 200

    def test_get_login_status_code(self):
        assert get_page('/login').status_code == 200

    def test_get_registration_status_code(self):
        assert get_page('/registration').status_code == 200


def test_create_existing_user():
    assert not add_new_user('user1', 'user1@gmail.com',
                            '08eaac4447cfe970111cb72c2dac27ea'
                            '1304d3b578f0a2288da6386ac0437543')
