def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x integers of a list on the same line followed
    Args:
       my_list (list, optional): The list to be printed. Defaults to [].
       x (int, optional): The number of elements to access in my_list.
           Defaults to 0 (prints all elements).

   Raises:
       IndexError: If x is greater than the length of the list.
   """

    count = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
    except IndexError:
        raise

    print()

    return count
