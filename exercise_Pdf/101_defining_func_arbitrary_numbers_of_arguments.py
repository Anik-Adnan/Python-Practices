# Arbitrary number of keyword arguments

def func(**kwargs):
    # kwargs will be a dictionary containing the names as keys and the values as values
    for name, value in kwargs.items():
        print(name, value)


func(value1=1, value2=2, value3=3)  # Calling it with 3 arguments
# Out: value1 1
# value2 2
# value3 3

func()  # Calling it without arguments
# No Out put

my_dict = {'foo': 1, 'bar': 2}
func(**my_dict)  # Calling it with a dictionary
# Out: foo 1
# bar 2

# You can't provide these without names, for example func(1, 2, 3) will raise a TypeError.
# kwargs is a plain native python dictionary. For example, args['value1'] will give the value for argument value1. Be
# sure to check beforehand that there is such an argument or a KeyError will be raised.

# Note on Nesting Functions with Optional Arguments
# It is possible to nest such functions and the usual convention is to remove the items that the code has already
# handled but if you are passing down the parameters you need to pass optional positional args with a * prefix and
# optional keyword args with a ** prefix, otherwise args with be passed as a list or tuple and kwargs as a single
# dictionary. e.g.:


def fn(**kwargs):
    print(kwargs)
    f1(**kwargs)


def f1(**kwargs):
    print(len(kwargs))


fn(a=1, b=2)
# Out:
# {'a': 1, 'b': 2}
# 2
