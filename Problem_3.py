def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1     # left = 2*i + 1
    right = 2 * i + 2     # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if left < n and arr[largest] < arr[left]:
        largest = left

    # See if right child of root exists and is
    # greater than root
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

# The main function to sort an array of given size


def heapSort(arr):
    """
    :param arr: is a list that we want to sort it.
    :return: None
    """
    n = len(arr)

    # Build a max heap.
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


def reverse(array):
    """
    :param array: is a list that we want to reverse it.
    :return: a list that has the same element but in reverse order.
    """
    list_ = []
    # traverse  array in reverse order and add to the new array.
    for i in range(len(array)-1, -1, -1):
        list_.append(array[i])

    return list_


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # if the list is empty or contains one element.
    if len(input_list) == 0 or len(input_list) == 1:
        return input_list

    # sort input_list
    heapSort(input_list)
    # reverse input_list
    input_list = reverse(input_list)

    s1 = ''
    s2 = ''

    # add the highest number in s1 skip 2 then add anther element, start this proses from index zero.
    for i in range(0, len(input_list), 2):
        s1 += str(input_list[i])

    # add the highest number in s2 skip 2 then add anther element, start this proses from index one.
    for i in range(1, len(input_list), 2):
        s2 += str(input_list[i])

    # convert s1 and s2 to integer create new array and then put s1 in index zero and s2 in index one.
    return [int(s1), int(s2)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


# Test case 1
test_function([[1, 2, 3, 4, 5], [542, 31]])  # return pass, this list with an odd number of elements.

# Test case 2
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])  # return pass, this list with an even number of elements.

# Test case 3
test_function([[], []])  # return pass.

# Test case 4
test_function([[1], [1]])  # return pass.
