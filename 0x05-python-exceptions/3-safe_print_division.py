def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
        return None
    finally:
        print("Inside result: {:d}".format(result))
    return result
