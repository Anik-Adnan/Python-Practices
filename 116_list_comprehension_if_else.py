# [x for x in 'apple' if x in 'aeiou' else '*']
# SyntaxError: invalid syntax
# When using if/else together use them before the loop

a = [x if x in 'aeiou' else '*' for x in 'apple']
print(a)
#['a', '*', '*', '*', 'e']