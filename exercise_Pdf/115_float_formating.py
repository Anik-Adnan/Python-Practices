print('{0:.3f}'.format(42.12345))
# '42.123'
print('{0:.7f}'.format(42.12345))
# '42.1234500'

# Same hold for other way of referencing:
print('{answer:.3f}'.format(answer=42.12345))
# '42.123'

# Floating point numbers can also be formatted in scientific notation or as percentages:
print('{0:.3e}'.format(42.12345))
# '4.212e+01'
print('{0:.0%}'.format(42.12345))
# '4212%'


# You can also combine the {0} and {name} notations. This is especially useful when you want to round all variables
# to a pre-specified number of decimals with 1 declaration:
s = 'Hello'
a, b, c = 1.12345, 2.34567, 34.5678
digits = 2
print('{0}! {1:.{n}f}, {2:.{n}f}, {3:.{n}f}'.format(s, a, b, c, n=digits))
# 'Hello! 1.12, 2.35, 34.57'
