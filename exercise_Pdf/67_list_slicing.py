# Using the third "step" argument
lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(lst[::2])  # ['a', 'c', 'e', 'g']
print(lst[::3])  # ['a', 'd', 'g']

# Selecting a sublist from a list
lst = ['a', 'b', 'c', 'd', 'e']
print(lst[2:4])  # ['c', 'd']
print(lst[2:])  # ['c', 'd', 'e']
print(lst[:4])  # ['a', 'b', 'c', 'd']

# Reversing a list with slicing
a = [1, 2, 3, 4, 5]
# steps through the list backwards (step=-1)
b = a[::-1]
# built-in list method to reverse 'a'
a.reverse()
if a is b:
    print(True)
print(b)
# Output:
# True
# [5, 4, 3, 2, 1]
