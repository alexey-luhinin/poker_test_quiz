"""Tests login.py"""
import pytest
from services.login import check_username


@pytest.mark.parametrize('username, password, expected',
                         [('barrrrygold',
                           'ee6c9997ac30643cfa51d1ffc04c0a7e63'
                           'bf39cb151a2c7f22846c17d7aa4d5e',
                           True)])
def test_check_username(username, password, expected):
    """Test_check_username"""
    assert check_username(username, password) == expected
