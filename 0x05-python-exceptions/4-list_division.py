def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        for i in range(list_length):
            try:
                if i < len(my_list_1) and i < len(my_list_2):
                    if isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float)):
                        if my_list_2[i] != 0:
                            result.append(my_list_1[i] / my_list_2[i])
                        else:
                            print("division by 0")
                            result.append(0)
                    else:
                        print("wrong type")
                        result.append(0)
                else:
                    print("out of range")
                    result.append(0)
            except ZeroDivisionError:
                print("division by 0")
                result.append(0)
    except Exception as e:
        print("Error:", e)
    finally:
        return result
