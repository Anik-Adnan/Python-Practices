# List Comprehension with nested loop
print([x + y for x in [1, 2, 3] for y in [3, 4, 5]])
#Out: [4, 5, 6, 5, 6, 7, 6, 7, 8]

# Nested List Comprehension
print([[x + y for x in [1, 2, 3]] for y in [3, 4, 5]])
#Out: [[4, 5, 6], [5, 6, 7], [6, 7, 8]]
# same as
# l = []
# for y in [3, 4, 5]:
#     temp = []
#     for x in [1, 2, 3]:
#         temp.append(x + y)
#     l.append(temp)


# One example where a nested comprehension can be used it to transpose a matrix.
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
m = [[row[i] for row in matrix] for i in range(len(matrix))]
print(m)
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
l = []
for i in range(len(matrix)):
    temp = []
    for row in matrix:
        temp.append(row[i])
    l.append(temp)
print(l)


# Like nested for loops, there is no limit to how deep comprehensions can be nested.
[[[i + j + k for k in 'cd'] for j in 'ab'] for i in '12']
# Out: [[['1ac', '1ad'], ['1bc', '1bd']], [['2ac', '2ad'], ['2bc', '2bd']]]
