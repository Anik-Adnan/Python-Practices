def decorators_funccton(any_function):
    def wrapper_function(*args, **kwargs):
        print('this is awesome function')
        return any_function(*args, **kwargs)
    return wrapper_function


@decorators_funccton
def func1(a):
    print(f'function with argument {a}')


func1(10)
# this is awesome function
# function with argument 10


@decorators_funccton
def add(a, b):
    return a + b


print(add(20, 5))  # for print 5 must return any_function
