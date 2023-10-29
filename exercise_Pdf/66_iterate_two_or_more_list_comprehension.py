# For iterating more than two lists simultaneously within list comprehension, one may use zip() as:
list_1 = [1, 2, 3, 4]
list_2 = ['a', 'b', 'c', 'd']
list_3 = ['6', '7', '8', '9']
# Two lists
print([(i, j) for i, j in zip(list_1, list_2)])
# [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# Three lists
print([(i, j, k) for i, j, k in zip(list_1, list_2, list_3)])
# [(1, 'a', '6'), (2, 'b', '7'), (3, 'c', '8'), (4, 'd', '9')]
# so on ...
