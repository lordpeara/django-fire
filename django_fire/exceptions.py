

class FireException(Exception):
    """Base exception for django_fire
    """


class FiredPassword(FireException):
    """Password is fired by staff's operation
    """
