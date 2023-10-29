# The format() method can be used to change the alignment of the string. You have to do it with a format expression
# of the form :[fill_char][align_operator][width] where align_operator is one of:

# < forces the field to be left-aligned within width.
# > forces the field to be right-aligned within width.
# ^ forces the field to be centered within width.
# = forces the padding to be placed after the sign (numeric types only).

# fill_char (if omitted default is whitespace) is the character used for the padding.
print('{:~<9s}, World'.format('Hello'))
# 'Hello~~~~, World'
print('{:~>9s}, World'.format('Hello'))
# '~~~~Hello, World'
print('{:~^9s}'.format('Hello'))
# '~~Hello~~'


print('{:0=6d}'.format(-123))
# '-00123'
foo = 'bar'
print(f'{foo:*^8s}')

# The format strings can also be nested:
price = 478.23
print(f"{f'${price:0.2f}':*>20s}")
# '*************$478.23'


print('{:.>{}}'.format('foo', 10))
# '.......foo'
print('{:{}{}{}}'.format('foo', '*', '^', 15))
# '******foo******'

data = ["a", "bbbbbbb", "ccc"]
m = max(map(len, data))
for d in data:
    print('{:>{}}'.format(d, m))
    print(f'{d:>{m}}')
# a
# bbbbbbb
# ccc
