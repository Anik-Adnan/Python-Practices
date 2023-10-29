# Comparison

# If elements are of the same type, python performs the comparison and returns the result. If elements are different
# types, it checks whether they are numbers.
# If numbers, perform comparison.
# If either element is a number, then the other element is returned.
# Otherwise, types are sorted alphabetically .

# If we reached the end of one of the lists, the longer list is "larger." If both list are same it returns 0.

tuple1 = ('a', 'b', 'c', 'd', 'e')
tuple2 = ('1', '2', '3')
tuple3 = ('a', 'b', 'c', 'd', 'e')
# comp = cmp(tuple1, tuple2)
# print(comp)  # Out: 1
# cmp(tuple2, tuple1)
# #Out: -1
# cmp(tuple1, tuple3)
# #Out: 0

# Tuple Length
# The function len returns the total length of the tuple
print(len(tuple1))  # Out: 5

# Max of a tuple
# The function max returns item from the tuple with the max value
print(max(tuple1))  # Out: 'e'
print(max(tuple2))  # Out: '3'

# Min of a tuple
# The function min returns the item from the tuple with the min value
print(min(tuple1))  # Out: 'a'
print(min(tuple2))  # Out: '1'

# Convert a list into tuple
# The built-in function tuple converts a list into a tuple.
list = [1, 2, 3, 4, 5]
print(tuple(list))  # Out: (1, 2, 3, 4, 5)


# Tuple concatenation
# Use + to concatenate two tuples
print(tuple1 + tuple2)  # Out: ('a', 'b', 'c', 'd', 'e', '1', '2', '3')
