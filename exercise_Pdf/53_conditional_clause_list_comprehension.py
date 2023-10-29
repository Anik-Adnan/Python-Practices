import time


def f(x):

    # time.sleep(.1)  # Simulate expensive function
    return x**2


# a = [f(x) for x in range(21) if f(x) > 10]
# print(a)  # [16, 25, 36, ...]

# the expensive operation only once for each value of x by generating an intermediate iterable (generator expression) as follows:
# a = [v for v in (f(x) for x in range(21)) if v > 10]
# print(a)  # [16, 25, 36, ...]

# using the builtin map equivalent:
# a = [v for v in map(f, range(21)) if v > 10]
# print(a)  # [16, 25, 36, ...]

a = [v for x in range(1000) for v in [f(x)] if v > 10]
print(a)


# def process_prime_numbers(iterable):
#     for x in iterable:
#         if is_pime(x): # need prime code
#             yield f(x)


# l = [x for x in process_prime_numbers(range(1000)) if x > 10]
# print(l)  # [11, 13, 17, 19, ...]
