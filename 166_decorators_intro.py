# decorators - enhence the function of the other function
# @ use for decorator

def decorators_funccton(any_function):
    def wrapping_function():
        print('this is decorators function')
        any_function()
    return wrapping_function


@decorators_funccton
def func1():
    print('function 1')


@decorators_funccton
def func2():
    print('function 2')

# without using @decorator_function
# func1() # function 1
# func2() # funtion 2

# func1 = decorators_funccton(func1)
# func1()


# using @decorator_function line defore function
func2()
# this is decorators function
# function 2
