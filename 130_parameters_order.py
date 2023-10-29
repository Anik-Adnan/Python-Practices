# function with all parameters
# very important to understand

# PADK

# parameter
# *args
# default parameters
# **kwargs

# def func(name= 'unknown' , age = 25): # default parameter
#     print(name)
#     print(age)
# func()
# func('adnan')
# func('anik',20) # normal parameter

def func(name, *args , last_name= 'unknown', **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)
func('anik', 1,2,3, 'adnan' ,a=1, b =2)