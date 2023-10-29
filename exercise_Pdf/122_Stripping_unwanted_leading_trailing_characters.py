# Three methods are provided that offer the ability to strip leading and trailing characters from a string: str.strip,
# str.rstrip and str.lstrip. All three methods have the same signature and all three return a new string object
# with unwanted characters removed.

# str.strip([chars])
# str.strip acts on a given string and removes(strips) any leading or trailing characters contained in the argument
# chars
# if chars is not supplied or is None, all white space characters are removed by default. For example:
print("     a line with leading and trailing space     ".strip())
# 'a line with leading and trailing space'


# If chars is supplied, all characters contained in it are removed from the string, which is returned. For example:
# strips '>' character and space character
print(">>> a Python prompt".strip('> '))
# 'a Python prompt'


# str.rstrip([chars]) and str.lstrip([chars])
# These methods have similar semantics and arguments with str.strip(), their difference lies in the direction from
# which they start. str.rstrip() starts from the end of the string while str.lstrip() splits from the start of the
# string.

print("     spacious string     ".rstrip())
# ' spacious string'

print("     spacious string ".lstrip())
# 'spacious string
