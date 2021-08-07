def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       :param input_list: Input array to search and the target
       :param number: our target we have to search in input_list to find it.
    Returns:
       int: Index or -1
    """
    if input_list is None or len(input_list) == 0:
        return -1

    cut = len(input_list)//2

    if input_list[cut] < input_list[cut-1]:
        cut -= 1

    item_1 = binary_search(input_list[cut + 1:], number)
    item_2 = binary_search(input_list[:cut + 1], number)

    if item_1 != -1:
        item_1 += cut + 1
        return item_1

    if item_2 != -1:
        return item_2

    return -1


def binary_search(array, target):

    """
    Write a function that implements the binary search algorithm using iteration

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    """

    low = 0
    high = len(array)-1

    while low <= high:

        mid = int((high + low)/2)
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            high = mid - 1

        elif array[mid] < target:
            low = mid+1

    return -1


def linear_search(input_list, number):

    if input_list is None or len(input_list) == 0:
        return -1

    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])   # return 0
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])  # return 5
test_function([[6, 7, 8, 1, 2, 3, 4], 8])   # return 2
test_function([[6, 7, 8, 1, 2, 3, 4], 1])  # return 3
test_function([[6, 7, 8, 1, 2, 3, 4], 10])  # return -1
# up normal case
test_function([[], 9])  # return -1
test_function([None, 8])  # return -1
