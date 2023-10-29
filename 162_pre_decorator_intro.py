# first class function / closures

def square(a):
    return a ** 2


s = square
print(s(5))
print(square(5))
# same name
print(s.__name__)  # square
print(square.__name__)  # square
# same memory location
print(s)
print(square)
