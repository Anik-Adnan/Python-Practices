even_num = [x for x in range(10) if x % 2 == 0]
print(even_num)  # Out: [0, 2, 4, 6, 8]

both = [2 * (x if x % 2 == 0 else -1) + 1 for x in range(10)]
print(both)  # Out: [1, -1, 5, -1, 9, -1, 13, -1, 17, -1]
# The above code is equivalent to:
numbers = []
for x in range(10):
    if x % 2 == 0:
        temp = x
    else:
        temp = -1
    numbers.append(2 * temp + 1)
print(numbers)
