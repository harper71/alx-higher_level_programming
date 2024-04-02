import sys


def safe_print_integer_err(value):
    """

    Args:
        value (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        print("Exception:", e, file=sys.stderr)
        return False
