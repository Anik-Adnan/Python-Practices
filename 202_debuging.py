

# Steps for debugging
# 1. set trace
# 2. execute code line by line

import pdb
pdb.set_trace()

name = input('enter your name : ')
age = input('type your age : ')
print(f'helllo {name} your {age}')
age2 = int(age) + 5
print(f'{name} will be {age2} in next five years')


# l
# c
# n
