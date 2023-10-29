from functools import wraps


def decorators_funccton(any_function):
    @wraps(any_function)
    def wrapper_function(*args, **kwargs):
        '''this is wrapper function '''
        print('this is awesome function')
        return any_function(*args, **kwargs)
    return wrapper_function


@decorators_funccton
def add(a, b):
    """this is add function"""
    return a + b


# print(add(20, 5))  # for print 25 must return any_function


# without import (from functools import wraps)
# print(add.__doc__)  # this is wrapper function
# print(add.__name__)  # wrapper_function

print(add.__name__)  # add
print(add.__doc__)  # this is add function
