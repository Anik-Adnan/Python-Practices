# The .format() method can interpret a number in different formats, such as:
print('{:c}'.format(65))  # Unicode character
# 'A'
print('{:d}'.format(0x0a))  # base 10
# '10'
print('{:n}'.format(0x0a))  # base 10 using current locale for separators
# '10'

# Format integers to different bases (hex, oct, binary)
print('{0:x}'.format(10))  # base 16, lowercase - Hexadecimal
# 'a'
print('{0:X}'.format(10))  # base 16, uppercase - Hexadecimal
# 'A'
print('{:o}'.format(10))  # base 8 - Octal
# '12'
print('{:b}'.format(10))  # base 2 - Binary
# '1010'
print('{0:#b}, {0:#o}, {0:#x}'.format(42))  # With prefix
# '0b101010, 0o52, 0x2a'
print('8 bit: {0:08b}; Three bytes: {0:06x}'.format(42))  # Add zero padding
# '8 bit: 00101010; Three bytes: 00002a'
