# Reduce takes a function and a collection of items. It returns a value that is created by combining the items.
# This is a simple reduce. It returns the sum of all the items in the collection.
import functools
import operator

total = functools.reduce(lambda a, x: a + x, [0, 1, 2, 3, 4])
total_all = functools.reduce(operator.add, [0, 1, 2, 3, 4])
total_mull = functools.reduce(operator.mul, [1, 2, 3, 4])
print(total)  # 10
print(total_all)  # 10
print(total_mull)  # 24
