#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except (ZeroDivisionError, TypeError, ValueError):
        result = None
        return None
    else:
        return result
    finally:
        print("Inside result: {}".format(result))
        return result
