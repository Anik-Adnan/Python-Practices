from random import randrange

# list.sort() sorts a list in -place(meaning that it modifies the original list) and returns the value None. Therefore, it
# won't work as expected in a list comprehension:
l = [x.sort() for x in [[2, 1], [4, 3], [0, 1]]]
print(l)  # [None, None, None]

# Instead, sorted() returns a sorted list rather than sorting in - place:
l = [sorted(x) for x in [[2, 1], [4, 3], [0, 1]]]
print(l)  # [[1, 2], [3, 4], [0, 1]]

[print(x) for x in (1, 2, 3)]
# Instead use:
# for x in (1, 2, 3):
#     print(x)

rand_num = [randrange(1, 7) for _ in range(10)]
print(rand_num)  # [2, 3, 2, 1, 1, 5, 2, 4, 3, 5]
