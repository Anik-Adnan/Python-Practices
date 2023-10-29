# sort() – sorts the list in numerical and lexicographical order and returns None.

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 7]

a.reverse()
print(a)  # [7, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

a.sort()
print(a)  # [0, 1, 2, 3, 4, 5, 6, 7, 7, 8, 9]

# Sorts the list in numerical order
# Lists can also be reversed when sorted using the reverse = True flag in the sort() method.
a.sort(reverse=True)
print(a)  # [9, 8, 7, 7, 6, 5, 4, 3, 2, 1, 0]
