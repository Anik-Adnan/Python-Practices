print("XßΣ".casefold())
# 'xssσ'
print("XßΣ".lower())
# 'xßς

s = "This is a 'string'"
print(s.upper())
print(s.lower())
print(s.title())

# str.capitalize returns a capitalized version of the string, that is, it makes the first character have upper case and
# the rest lower:
s = "i am anik.i am a student."
print(s.capitalize())

# str.swapcase returns a new string object in which all lower case characters are swapped to upper case and all
# upper case characters to lower:
print(s.swapcase())

# Usage as str class methods
print(str.upper("This is a 'string'"))
# "THIS IS A 'STRING'"
print(list(map(str.upper, ["These", "are", "some", "'strings'"])))
# ['THESE', 'ARE', 'SOME', "'STRINGS'"]

print(s.find('a', 3))
print(s.replace('am', 'was', 2))
c = 'Anik'
print(c.center(10, '*'))
print(f"{c:*^10}")
