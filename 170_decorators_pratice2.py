# calculate run time of a function
from functools import wraps
import time
t1 = time.time()


def calculate_time(func):
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        t1 = time.time()
        returned_value = func(*args, **kwargs)
        t2 = time.time()
        total_time = t2-t1
        print(f'this {func.__name__} function took {total_time} sec to run')
        return returned_value
    return wrapper_func


@calculate_time
def add(a, b):
    return f'sum = {a + b}'


print(add(50, 50))
