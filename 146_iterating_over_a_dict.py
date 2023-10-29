d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key, d[key])

for key, value in d.items():
    print(key, value)

print([key for key in d])

for key in d.keys():
    print(key)


for value in d.values():
    print(value)
