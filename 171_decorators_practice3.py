# only int allow
# @only_int_allow
from functools import wraps


def only_int_allow(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if all([type(arg) == int for arg in args]):
            return function(*args, **kwargs)
        print("Invalid argument")  # else
        # data_type = []
        # for arg in args:
        #     data_type.append(type(arg) == int)
        # if all(data_type):
        #     return function(*args, **kwargs)
        # else:
        #     print("Invalid argument")
    return wrapper


@only_int_allow
def add_all(*args):
    total = 0
    for i in args:
        total += i
    return total


print(add_all(1, 3, 2, 5))  # 11
print(add_all(1, 3, 2, 5, [2, 5, 7, 10]))
# Invalid argument
# None (because else does not return anything)
