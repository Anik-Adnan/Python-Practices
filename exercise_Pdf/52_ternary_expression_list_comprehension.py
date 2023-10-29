# One can combine ternary expressions and if conditions. The ternary operator works on the filtered result:

p = [x if x > 2 else '*' for x in range(10) if x % 2 == 0]
print(p)  # Out: ['*', '*', 4, 6, 8]

# The same couldn't have been achieved just by ternary operator only:
p = [x if (x > 2 and x % 2 == 0) else '*' for x in range(10)]
print(p)  # Out:['*', '*', '*', '*', 4, '*', 6, '*', 8, '*']
