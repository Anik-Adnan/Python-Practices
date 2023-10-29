# str.startswith(prefix[, start[, end]])
# As its name implies, str.startswith is used to test whether a given string starts with the given characters in
# prefix.
s = "This is a test string"
print(s.startswith("T"))  # True
print(s.startswith("Thi"))  # True
print(s.startswith("thi"))  # False


# The optional arguments start and end specify the start and end points from which the testing will start and finish.
# In the following example, by specifying a start value of 2 our string will be searched from position 2 and afterwards:
print(s.startswith("is", 2))  # True

# This yields True since s[2] == 'i' and s[3] == 's'.
# You can also use a tuple to check if it starts with any of a set of strings
print(s.startswith(('This', 'That')))  # True
print(s.startswith(('ab', 'bc')))  # False

print('\nendswith()\n')
# str.endswith(prefix[, start[, end]])
# str.endswith is exactly similar to str.startswith with the only difference being that it searches for ending
# characters and not starting characters.For example, to test if a string ends in a full stop, one could write:
s = "this ends in a full stop."
print(s.endswith('.'))  # True
print(s.endswith('!'))  # False

# as with startswith more than one characters can used as the ending sequence:
print(s.endswith('stop.'))  # True
print(s.endswith('Stop.'))  # False
# You can also use a tuple to check if it ends with any of a set of strings
print(s.endswith(('.', 'something')))  # True
print(s.endswith(('ab', 'bc')))  # False
