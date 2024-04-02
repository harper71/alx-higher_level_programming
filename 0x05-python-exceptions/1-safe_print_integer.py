def safe_print_integer(value):
    """prints value if it is an int
    Args:
        value (any type): takes any type of data
    Returns:
        boolean : true if value is integer else false
    """
    try:
        print("{:d}".format(int(value)))
        return True
    except ValueError:
        return False
