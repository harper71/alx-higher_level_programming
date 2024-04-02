#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Prints the elements of a list without a trailing newline.

    Args:
        my_list (list, optional): The list to be printed. Defaults to [].
        x (int, optional): The number of elements to print.
            If x is greater than the length of the list
            Defaults to 0 (prints all elements).

    Returns:
        int: The number of elements actually printed.
    """

    count = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            count += 1
    except IndexError:
        for i in my_list:
            print("{}".format(i), end=" ")
            count += 1
        pass
    print()

    return count
