# filter (python 3.x) return a generator so they can be very handy when creating a shortcircuit
# test like or or and:

car_shop = [('Toyota', 1000), ('rectangular tire', 80), ('Porsche', 5000)]


def find_something_smaller_than(name_value_tuple):
    print('Check {0}, {1}$'.format(*name_value_tuple))
    return name_value_tuple[1] < 100


print(next(filter(find_something_smaller_than, car_shop)))
# Print: Check Toyota, 1000$
# Check rectangular tire, 80$
# Out: ('rectangular tire', 80)

# The next-function gives the next (in this case first) element of and is therefore the reason why it's short-circuit.


# Using an equivalent generator:
car_shop = [('Toyota', 1000), ('rectangular tire', 80), ('Porsche', 5000)]
generator = (car for car in car_shop if not car[1] < 100)
print(next(generator))
