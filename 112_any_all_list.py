nums = [1, 1, 0, 1]
# all() to determine if all the values in an iterable evaluate to True
print(all(nums))
# False
chars = ['a', 'b', 'c', 'd']
print(all(chars) )
# True

# any() determines if one or more values in an iterable evaluate to True
nums = [1, 1, 0, 1]
print(any(nums))
# True
vals = [None, None, None, False]
print(any(vals))
# False

vals = [1, 2, 3, 4]
print(any(val > 12 for val in vals))
# False

print(any((val * 2) > 6 for val in vals))
# True