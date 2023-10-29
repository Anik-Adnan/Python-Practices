def shift_list(array, s):
    """
    Shifts the elements of a list to the left or right.
    Args:
        array - the list to shift
        s - the amount to shift the list ('+': right-shift, '-': left-shift)
    Returns:
        shifted_array - the shifted list """


# calculate actual shift amount (e.g., 11 --> 1 if length of the array is 5)
    s %= len(array)
# reverse the shift direction to be more intuitive
    s *= -1
# shift array with list slicing
    shifted_array = array[s:] + array[:s]
    return shifted_array


my_array = [1, 2, 3, 4, 5]
# negative numbers
print(shift_list(my_array, -7))
# [3, 4, 5, 1, 2]
# no shift on numbers equal to the size of the array
print(shift_list(my_array, 5))
# [1, 2, 3, 4, 5]
# works on positive numbers
print(shift_list(my_array, 4))  # [2, 3, 4, 5, 1]
print(shift_list(my_array, 3))  # [3, 4, 5, 1, 2]
print(shift_list(my_array, 2))  # [4, 5, 1, 2, 3]
