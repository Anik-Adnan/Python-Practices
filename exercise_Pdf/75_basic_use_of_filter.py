names = ['Anik', 'Farhad', 'Momotuz']


def long_name(name):
    return len(name) > 6


print(list(filter(long_name, names)))
# ['Momotuz']

# equivalent list comprehension
print([name for name in names if len(name) > 6])

# equivalent generator expression
print(list((name for name in names if len(name) > 6)))
