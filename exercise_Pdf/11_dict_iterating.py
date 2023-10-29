d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
    print(key)
# a
# b
# c

print([key for key in d])
# ['a', 'b', 'c']

for key in d:
    print(key, d[key])
# a 1
# b 2
# c 3
for key, value in d.items():
    print(key, value)
# a 1
# b 2
# c 3

for value in d.values():
    print(value)
# 1
# 2
# 3
