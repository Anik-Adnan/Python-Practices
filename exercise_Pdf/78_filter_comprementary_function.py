# Usage without function (None):
list(filter(None, [1, 0, 2, [], '', 'a']))  # discards 1, 2, 'a'
# Out: [0, [], '']
# Usage with function
names = ['anik', 'adnan', 'farhad']


def long_name(name):
    return len(name) > 5


print(list(filter(long_name, names)))
# Out: ['farhad']

# Short-circuit usage with next:
car_shop = [('Toyota', 1000), ('rectangular tire', 80), ('Porsche', 5000)]


def find_something_smaller_than(name_value_tuple):
    print('Check {0}, {1}$'.format(*name_value_tuple))
    return name_value_tuple[1] < 100


print(next(filter(find_something_smaller_than, car_shop)))
# Print: Check Toyota, 1000$
# Out: ('Toyota', 1000)


# Using an equivalent generator:
car_shop = [('Toyota', 1000), ('rectangular tire', 80), ('Porsche', 5000)]
generator = (car for car in car_shop if not car[1] < 100)
print(next(generator))
