import pytest
from utils import get_hash256, str_to_b64
from config import SECRET_KEY
from services.registration import (
    check_username_format,
    check_email_format,
    check_password_format,
    is_same_password,
    add_new_user,
)
from models import User, db


@pytest.mark.parametrize(
    'username, expected', [
        ('barrrrygold', True),
        ('alex11', True),
        ('alex$@yes', True),
        ('barrrry gold', False),
        ('', False),
        ('vova', False),
        ('1vova', False),
        ('aaaaaaaaaaaaaaaaaaaaaaaaaa', False),
        ('alexэтоя', False),
    ]
)
def test_check_username_format(username, expected):
    """Tests for username_format"""
    assert check_username_format(username) == expected


@pytest.mark.parametrize(
    'email, expected', [
        ('podzakon11@gmail.com', True),
        ('m0679492571@gmail.com', True),
        ('mr.black@google.com', True),
        ('verynice@gmail.com', True),
        ('ZZZcat777@mail.ru', True),
        ('0673335743@ukr.net', True),
        ('Malahova-T@rambler.ru', True),
        ('001138@domena.net', True),
        ('666-morgenstern&gmail.com', False),
        ('mr.black@google,com', False),
    ]
)
def test_check_email_format(email, expected):
    """Tests for email_format"""
    assert check_email_format(email) == expected


@pytest.mark.parametrize(
    'password, expected', [
        (r'root', False),
        (r'alexey', False),
        (r'AlexeyLuhinin', False),
        (r'alex123', False),
        (r'Fedor112', False),
        (r'Fedor112 Cool', False),
        (r'password123', False),
        (r';6XYC-hu', True),
        (r'U^}ChW9c,?z.;">_', True),
        (r'eymT\5JMh_r4V{+h', True),
        (r'B^,5vY^Z`hN#{M4R', True),
    ]
)
def test_check_password_format(password, expected):
    """Tests for email_format"""
    assert check_password_format(password) == expected


def test_is_same_password():
    """Tests for checks equals password and re-password"""
    assert is_same_password('alexey123', 'alexey123')
    assert not is_same_password('alexey123', 'fedor')


class TestAddNewUser:
    def setup(self):
        self.username = 'user2'
        self.email = 'user2@gmail.com'
        self.password = 'User2User2!'

    def test_create_new_user(self):
        hashed_password = get_hash256(str_to_b64(self.password)+SECRET_KEY)
        assert add_new_user(self.username, self.email, hashed_password)

    def teardown(self):
        User.query.filter_by(username=self.username).delete()
        db.session.commit()
