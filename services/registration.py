"""Contains functions for registration users"""
import re
from collections import namedtuple
from utils import has_uppercase, has_digit, has_special_symbol
import models


Error = namedtuple('Error', ['username_format',
                             'email_format',
                             'password_format',
                             'passwords_not_equals',
                             'username_is_same'])

error = Error(
    username_format='* Username must be between 5 and 25 characters.<br>\
                     * Consists of Latin letters and starts with a letter.<br>\
                     * Must not contain spaces.',
    email_format='Wrong format of email',
    password_format='* The password must be 8 or more characters long.<br>\
                     * The password must not contain spaces.<br>\
                     * The password must contain at least one number.<br>\
                     * The password must contain at least \
                     one capital letter.<br>\
                     * The password must contain at least one special \
                     character, such as @#!...',
    passwords_not_equals='Passwords are not equals.',
    username_is_same='Username is already in use, choose another username!',
)


def is_same_password(password: str, re_password: str) -> bool:
    """checks two passwords to equal"""
    return password == re_password


def check_password_format(password: str) -> bool:
    """requirements to password:
    * at least 8 characters—the more characters, the better
    * not contains whitespaces
    * at least 1 uppercase letter
    * at least 1 number
    * inclusion of at least one special character, e.g., ! @ # ? ]
    """
    if len(password) < 8:
        return False

    if ' ' in password:
        return False

    if not has_uppercase(password):
        return False

    if not has_digit(password):
        return False

    if not has_special_symbol(password):
        return False

    return True


def check_email_format(email: str) -> bool:
    """Checks format of email"""
    email_regex = re.compile(r'[^@]+@[^@]+\.[^@]+')
    return bool(email_regex.match(email))


def check_username_format(username: str) -> bool:
    """Requirements to username:
    * Have 25 >= length >= 5
    * Starts with a letter
    * Contains only ascii symbols
    * Doesn't contains spaces
    """
    if not 25 >= len(username) >= 5:
        return False

    if ' ' in username:
        return False

    if not username.isascii():
        return False

    if not username[0].isalpha():
        return False

    return True


def add_new_user(username: str, email: str,
                 password: str, group='student') -> None:
    """Create new user in database"""
    try:
        models.db.session.add(models.User(username=username,
                                          email=email,
                                          password=password, group=group))
        models.db.session.commit()
        return True
    except:
        return False
