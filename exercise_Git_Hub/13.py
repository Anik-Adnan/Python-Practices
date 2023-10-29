# Write a program that accepts a sentence and calculate
# the number of letters and digits.
# input
# hello world! 123
# output
# LETTERS 10
# DIGITS 3

# s = input()
# d = {"DIGITS": 0, "LETTERS": 0}
# for c in s:
#     if c.isdigit():
#         d["DIGITS"] += 1
#     elif c.isalpha():
#         d["LETTERS"] += 1
#     else:
#         pass
# print("LETTERS", d["LETTERS"])
# print("DIGITS", d["DIGITS"])


# or
import re
word = input()
letter, digit = 0, 0

for i in word:
    if ('a' <= i and i <= 'z') or ('A' <= i and i <= 'Z'):
        letter += 1
    if '0' <= i and i <= '9':
        digit += 1

print("LETTERS {0}\nDIGITS {1}".format(letter, digit))


# or
word = input()
letter, digit = 0, 0

for i in word:
    if i.isalpha():  # returns True if alphabet
        letter += 1
    elif i.isnumeric():  # returns True if numeric
        digit += 1
# two different types of formating method is shown in both solution
print(f"LETTERS {letter}\n{digit}")


# or
#''' Solution by: popomaticbubble'''

# input_string = input('> ')
# print()
# counter = {"LETTERS": len(re.findall(
#     "[a-zA-Z]", input_string)), "NUMBERS": len(re.findall("[0-9]", input_string))}

# print(counter)
