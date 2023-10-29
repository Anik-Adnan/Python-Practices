def greeting():
    return "Hello"


print(greeting())
# prints:
#     Hello

# This can be written as a lambda function as follows:

# greet_me = lambda: "Hello"
# print(greet_me())


def greet_me(): return "Hello"


print(greet_me())

# lambdas can take arguments, too:


def strip_and_upper_case(s): return s.strip().upper()


print(strip_and_upper_case(" Hello "))

# returns the string:
# HELLO
