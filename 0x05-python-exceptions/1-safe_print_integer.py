#!/usr/bin/python3
def safe_print_integer(value):
    """Print an integer with "{:d}".format().
    Args:
        value (int): The integer to print.
    Returns:
        If a TypeError, ValueError, or OverflowError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError, OverflowError):
        return False
