# The dict() constructor can be used to create dictionaries from keyword arguments, or from a single iterable of
# key-value pairs, or from a single dictionary and keyword arguments.
print(dict(a=1, b=2, c=3))  # {'a': 1, 'b': 2, 'c': 3}
print(dict([('d', 4), ('e', 5), ('f', 6)]))  # {'d': 4, 'e': 5, 'f': 6}
print(dict([('a', 1)], b=2, c=3))  # {'a': 1, 'b': 2, 'c': 3}
print(dict({'a': 1, 'b': 2}, c=3))  # {'a': 1, 'b': 2, 'c': 3}
