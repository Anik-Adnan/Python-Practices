def count_x(l, c):
    count = 0
    for i in l:
        if i == c:
            count += 1
    return count


l = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print('{} has occurred {} times'.format(x, count_x(l, x)))

# using count method
c = l.count(x)
print(x, " has ", c, " times.")
