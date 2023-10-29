# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8]
# print(list(zip(a, b))) #l = [(1, 5), (2, 6), (3, 7), (4, 8)]

l = [(1, 5), (2, 6), (3, 7), (4, 8)]
# * operator with zip
print(list(zip(*l)))
x, y = list(zip(*l))
print(x)  # (1, 2, 3, 4)
print(y)  # (5, 6, 7, 8)


a = [1, 10, 2, 15]
b = [50, 6, 35, 8]
new_list = []
for pair in zip(a, b):
    # print(pair)
    new_list.append(max(pair))
print(new_list)
