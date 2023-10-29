def add(a, b):
    return a + b


# print(add(5, 10))
# print(add('5', '10'))


def Add(a, b):
    if (type(a) is int) and (type(b) is int):
        return a + b
    return 'you are passing wrong data type to function'


# print(Add('5', '10'))
# print(Add(5, 10))


def Add2(a, b):
    if (type(a) is int) and (type(b) is int):
        return a + b
    raise TypeError('OOPs! you are passing wrong data type to function')


print(Add2('5', '10'))
# print(Add(5, 10))
