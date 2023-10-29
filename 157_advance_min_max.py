num1 = [1, 3,  4, 5]
num2 = [10, 20, 3, 40, 500]
print(min(num1))
print(max(num2))

# maximum length and itemvalue
name = ['a', 'ank', 'asif', 'rahid', 'momotuz', 'b']
max_len = list(zip(map(len, name), name))
print(max(max_len))
print(min(max_len))


def func(item):
    return len(item)


name = ['a', 'ank', 'asif', 'rahid', 'momotuz', 'b']
print(max(name, key=func))
print(min(name, key=func))
print(max(name, key=lambda item: len(item)))
print(min(name, key=lambda item: len(item)))
