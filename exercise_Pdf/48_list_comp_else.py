# create a list of characters in apple, replacing non vowels with '*'
# Ex - 'apple' --> ['a', '*', '*', '*' ,'e']

# [x for x in 'apple' if x in 'aeiou' else '*']
# SyntaxError: invalid syntax

# When using if/else together use them before the loop

l = [x if x in 'aeiou' else '*' for x in 'apple']
print(l)  # ['a', '*', '*', '*', 'e']
