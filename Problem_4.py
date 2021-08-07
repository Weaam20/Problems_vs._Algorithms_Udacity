def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    # if input_list was empty or equal to None.
    if input_list is None or len(input_list) == 0:
        return []

    size = len(input_list)
    output = [0] * size

    # Initialize count array
    count = [0] * 3

    # Store the count of each elements in count array
    for i in range(0, size):
        count[input_list[i]] += 1

    # Store the cumulative count
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[input_list[i]] - 1] = input_list[i]
        count[input_list[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        input_list[i] = output[i]

    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


# Test case 1
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])  # return pass
# Test case 2
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])  # return pass
# Test case 3
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])  # return pass
# ------------------------------------------------------------------------------- Invalid
# Test case 4
test_function([])  # return []
# Test case 5
test_function([])  # return []
