"""Tests login.py"""
import pytest
from services.login import check_username


@pytest.mark.parametrize('username, password, expected',
                         [('user1',
                           '08eaac4447cfe970111cb72c2dac27ea'
                           '1304d3b578f0a2288da6386ac0437543',
                           True)])
def test_check_username(username, password, expected):
    """Test_check_username"""
    assert check_username(username, password) == expected
