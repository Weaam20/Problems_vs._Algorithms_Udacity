def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    # if number is a negative number.
    if number < 0:
        return -1

    # create dictionary that store the square of the numbers from 0- number
    temp = {}
    for i in range(0, number+1):
        temp.update({i*i : i})
    # case 1 if number is square.
    if number in temp.keys():
        return temp[number]
    else:
        # case 2 if number is square.
        for num, index in temp.items():
            if number < num:
                # here I am try to find the two numbers between number.
                big_num = num
                small_num = (index-1)*(index-1)
                # difference between big_num and small_num.
                diff = big_num - small_num - 1
                # the half difference between big_num and small_num.
                h_diff = diff//2
                # part_1 is a part of numbers it is near to small_num.
                part_1 = small_num + h_diff
                # part_2 is a part of numbers it is near to big_num.
                part_2 = big_num - h_diff
                """
                 If number is smaller than part_1 or equal to part_1 then the root of number will be the same of 
                 the small_num.
                """
                if number <= part_1:
                    return temp[small_num]
                # else if number is bigger than part_2 then the root of number will be the same of the big_num.
                elif number > part_2:
                    return temp[big_num]


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
print("Pass" if (10 == sqrt(100)) else "Fail")
print("Pass" if (4 == sqrt(13)) else "Fail")
print("Pass" if (43 == sqrt(1876)) else "Fail")
print("Pass" if (-1 == sqrt(-10)) else "Fail")
