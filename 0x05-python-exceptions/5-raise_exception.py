def raise_exception():
    try:
        raise TypeError("Custom exception: This is a type error.")
    except TypeError as e:
        raise e
