# You can use all() to determine if all the values in an iterable evaluate to True
nums = [1, 1, 0, 1]

print(all(nums))  # False

chars = ['a', 'b', 'c', 'd']
print(all(chars))  # True

# Likewise, any() determines if one or more values in an iterable evaluate to True
nums = [1, 1, 0, 1]
print(any(nums))  # True

vals = [None, None, None, False]
print(any(vals))  # False

#####
vals = [1, 2, 3, 4]
any(val > 12 for val in vals)
# False
any((val * 2) > 6 for val in vals)
# True
