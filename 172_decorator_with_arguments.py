from functools import wraps


def only_data_type_allow(data_type):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if all([type(arg) == data_type for arg in args]):
                return function(*args, **kwargs)
            print("Invalid argument")  # else
        return wrapper
    return decorator


@only_data_type_allow(str)
def str_func(*args):
    string = ''
    for i in args:
        string += i
    return string


print(str_func('a', 'n', 'ik', ' ', 'ad', 'nan'))
