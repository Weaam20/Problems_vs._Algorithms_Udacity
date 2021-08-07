import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    # if list was empty or equal to None.
    if ints is None or len(ints) == 0:
        return None

    # in the beginning max_num and min_num equal to first element in the list.
    max_num = ints[0]
    min_num = ints[0]

    # find max element.
    for i in range(len(ints)):
        if ints[i] > max_num:
            max_num = ints[i]

    # find min element.
    for i in range(len(ints)):
        if ints[i] < min_num:
            min_num = ints[i]

    return min_num, max_num


# Example Test Case of Ten Integers
# Test case 1
list_ = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(list_)
print("Pass" if ((0, 9) == get_min_max(list_)) else "Fail")  # return pass

# Test case 2
list_ = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print("Pass" if ((1, 1) == get_min_max(list_)) else "Fail")  # return pass

# Test case 3
list_ = []
print("Pass" if (None is get_min_max(list_)) else "Fail")  # return pass

# Test case 4
list_ = None
print("Pass" if (None is get_min_max(list_)) else "Fail")  # return pass
