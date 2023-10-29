import string

# Concatenation of ascii_lowercase and ascii_uppercase:
print(string.ascii_letters)

# Contains all lower case ASCII characters:
print(string.ascii_lowercase)

# Contains all upper case ASCII characters:
print(string.ascii_uppercase)

# Contains all decimal digit characters:
print(string.digits)
print(string.hexdigits)
print(string.octdigits)

# Contains all characters which are considered punctuation in the C locale:
print(string.punctuation)

# Contains all ASCII characters considered whitespace:
# >>> string.whitespace
# ' \t\n\r\x0b\x0c'
print(string.whitespace)

# Contains all characters which are considered printable; a combination of string.digits, string.ascii_letters,
# string.punctuation, and string.whitespace.
print(string.printable)
