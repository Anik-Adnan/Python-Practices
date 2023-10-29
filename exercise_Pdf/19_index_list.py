# index(value, [startIndex]) – gets the index of the first occurrence of the input value. If the input value is
# not in the list a ValueError exception is raised. If a second argument is provided, the search is started at that
# specified index.

a = [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10]
print(a.index(7))
# Returns: 6
# print(a.index(49))  # ValueError, because 49 is not in a.

print(a.index(7, 7))  # starting search index 7
# Returns: 7

# print(a.index(7, 8))
# ValueError, because there is no 7 starting at index 8
