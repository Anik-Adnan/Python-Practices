# lambdas are commonly used for short functions that are convenient to define at the point where they are called
# (typically with sorted, filter and map).
# For example, this line sorts a list of strings ignoring their case and ignoring whitespace at the beginning and at the
# end:
p = sorted([" foo ", " bAR", "BaZ "], key=lambda s: s.strip().upper())
print(p)  # [' bAR', 'BaZ ', ' foo ']

# Sort list just ignoring whitespaces:
p2 = sorted([" foo ", " bAR", "BaZ "], key=lambda s: s.strip())
print(p2)  # ['BaZ ', ' bAR', ' foo ']


# Examples with map:
mp = sorted(map(lambda s: s.strip().upper(), [" foo ", " bAR", "BaZ "]))
print(mp)  # ['BAR', 'BAZ', 'FOO']
mp2 = sorted(map(lambda s: s.strip(), [" foo ", " bAR", "BaZ "]))
print(mp2)  # ['BaZ', 'bAR', 'foo']


# Examples with numerical lists:
my_list = [3, -4, -2, 5, 1, 7]
l1 = sorted(my_list, key=lambda x: abs(x))
print(l1)  # [1, -2, 3, -4, 5, 7]
l2 = list(filter(lambda x: x > 0, my_list))
print(l2)  # [3, 5, 1, 7]
l3 = list(map(lambda x: abs(x), my_list))
print(l3)  # [3, 4, 2, 5, 1, 7]


# One can call other functions (with/without arguments) from inside a lambda function.
def foo(msg):
    print(msg)


greet = lambda x = "hello world": foo(x)
greet()
# hello world
