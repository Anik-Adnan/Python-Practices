# Functions in python are first-class objects. They can be defined in any scope
def fibonacci(n):
    def step(a, b):
        return b, a+b
    a, b = 0, 1
    for _ in range(n):
        a, b = step(a, b)
    return a


print(fibonacci(5))
