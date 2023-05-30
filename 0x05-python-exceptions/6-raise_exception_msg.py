#!/usr/bin/python3
def raise_exception_msg(message=""):
    """Raise a CustomException exception with a message."""
    raise CustomException(message)

class CustomException(Exception):
    pass
