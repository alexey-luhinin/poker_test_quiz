"""Login"""
import models


def check_username(username: str, password: str) -> bool:
    """Checks username and password in db."""
    user = models.User.query.filter_by(username=username).first()
    if user:
        return user.password == password
    return False
