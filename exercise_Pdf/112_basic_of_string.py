foo = 1
bar = 'bar'
baz = 3.14

# You can use str.format to format output. Bracket pairs are replaced with arguments in the order in which the
# arguments are passed:
print('{}, {} and {}'.format(foo, bar, baz))
# Out: "1, bar and 3.14"

# Indexes can also be specified inside the brackets. The numbers correspond to indexes of the arguments passed to
# the str.format function (0-based).
print('{0}, {1}, {2}, and {1}'.format(foo, bar, baz))
# Out: "1, bar, 3.14, and bar

# Named arguments can be also used:
print("X value is: {x_val}. Y value is: {y_val}.".format(x_val=2, y_val=3))
# Out: "X value is: 2. Y value is: 3."

# Object attributes can be referenced when passed into str.format:


class AssignValue(object):
    def __init__(self, value):

        self.value = value


my_value = AssignValue(6)
print('My value is: {0.value}'.format(my_value))  # "0" is optional
# Out: "My value is: 6"


# Dictionary keys can be used as well:
my_dict = {'key': 6, 'other_key': 7}
print("My other key is: {0[other_key]}".format(my_dict))  # "0" is optional
# Out: "My other key is: 7"


# Same applies to list and tuple indices:
my_list = ['zero', 'one', 'two']
print("2nd element is: {0[2]}".format(my_list))  # "0" is optional
# Out: "2nd element is: two"
