# str.isalpha
# str.isalpha takes no arguments and returns True if the all characters in a given string are alphabetic, for example:

print("Hello World".isalpha())  # contains a space
# False
print("Hello2World".isalpha())  # contains a number
# False
print("HelloWorld!".isalpha())  # contains punctuation
# False
print("HelloWorld".isalpha())  # True
print("".isalpha())  # False


# str.isupper, str.islower, str.istitle

# These methods test the capitalization in a given string.
# str.isupper is a method that returns True if all characters in a given string are uppercase and False otherwise.
print("HeLLO WORLD".isupper())  # False
print("HELLO WORLD".isupper())  # True
print("".isupper())  # False

# Conversely, str.islower is a method that returns True if all characters in a given string are lowercase and False
# otherwise.
print("Hello world".islower())  # False
print("hello world".islower())  # True
print("".islower())  # False

# str.istitle returns True if the given string is title cased; that is, every word begins with an uppercase character
# followed by lowercase characters.
print("hello world".istitle())  # False
print("Hello world".istitle())  # False
print("Hello World".istitle())  # True
print("".istitle())  # False

# str.isdecimal, str.isdigit, str.isnumeric
# str.isdecimal returns whether the string is a sequence of decimal digits, suitable for representing a decimal
# number.
# str.isdigit includes digits not in a form suitable for representing a decimal number, such as superscript digits.
# str.isnumeric includes any number values, even if not digits, such as values outside the range 0 - 9.

# str.isalnum
# This is a combination of str.isalpha and str.isnumeric, specifically it evaluates to True if all characters in the
# given string are alphanumeric, that is, they consist of alphabetic or numeric characters:
print("Hello2World".isalnum())  # True
print("HelloWorld".isalnum())  # True
print("2016".isalnum())  # True
print("Hello World".isalnum())  # contains whitespace
# False


print('str.isspace')
# Evaluates to True if the string contains only whitespace characters.
print("\t\r\n".isspace())  # True
print(" ".isspace())  # True
# Sometimes a string looks “empty” but we don't know whether it's because it contains just whitespace or no
# character at all
print("".isspace())  # False

# To cover this case we need an additional test
my_str = ''
my_str.isspace()
# False
print(my_str.isspace() or not my_str)
# True
# But the shortest way to test if a string is empty or just contains whitespace characters is to use strip(with no
# arguments it removes all leading and trailing whitespace characters)
print(not my_str.strip())
# True
