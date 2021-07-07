"""Tests for utils.py"""
import pytest
from utils import str_to_b64, get_hash256
from config import SECRET_KEY


@pytest.mark.parametrize(
    'text, expected', [
        ('barrrrygold', 'YmFycnJyeWdvbGQ='),
        ('admin', 'YWRtaW4='),
    ]
)
def test_str_to_b64(text, expected):
    """Tests for str_to_b64"""
    assert str_to_b64(text) == expected


@pytest.mark.parametrize(
    'text, expected', [
        ('barrrrygold',
         '59b3e61dbd28c722a2b1c420ce9d994e6f251529a7968910c3c9ee4dfec07ef7'),
        ('admin',
         '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918'),
        (str_to_b64('podzakoN11!')+SECRET_KEY,
         'ee6c9997ac30643cfa51d1ffc04c0a7e63bf39cb151a2c7f22846c17d7aa4d5e'),
    ]
)
def test_get_hash256(text, expected):
    """Tests for get_hash256"""
    assert get_hash256(text) == expected
