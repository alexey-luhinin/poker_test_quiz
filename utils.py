"""Utils"""
from string import punctuation
from base64 import b64encode
from hashlib import sha256


def has_uppercase(text: str) -> bool:
    """Returns True if text has uppercase letter otherwise returns False"""
    for char in text:
        if char.isupper():
            return True

    return False


def has_digit(text: str) -> bool:
    """Returns True if text has digit otherwise returns False"""
    for char in text:
        if char.isdigit():
            return True

    return False


def has_special_symbol(text: str) -> bool:
    """Returns True if text has special symbols otherwise returns False"""
    for char in text:
        if char in punctuation:
            return True

    return False


def str_to_b64(text: str) -> str:
    """Converts input str to str encoded by base64."""
    return b64encode(text.encode('UTF-8')).decode('UTF-8')


def get_hash256(text: str) -> str:
    """Returns hash used sha256 from str."""
    return sha256(text.encode('UTF-8')).hexdigest()
