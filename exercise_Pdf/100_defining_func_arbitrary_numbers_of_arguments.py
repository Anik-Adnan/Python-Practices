# Arbitrary number of positional arguments:

def func(*args):
    # args will be a tuple containing all values that are passed in
    for i in args:
        print(i)


func(1, 2, 3)  # Calling it with 3 arguments
# Out: 1
# 2
# 3
list_of_arg_values = [1, 2, 3]
func(*list_of_arg_values)  # Calling it with list of values, * expands the list
# Out: 1
# 2
# 3
func()  # Calling it without arguments
# No Output


# You can't provide a default for args, for example func(*args=[1, 2, 3]) will raise a syntax error (won't even
# compile).
# You can't provide these by name when calling the function, for example func(*args=[1, 2, 3]) will raise a
# TypeError.
# But if you already have your arguments in an array (or any other Iterable), you can invoke your function like this:
# func(*my_stuff).
# These arguments (*args) can be accessed by index, for example args[0] will return the first argument
