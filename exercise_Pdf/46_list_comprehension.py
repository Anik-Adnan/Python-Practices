squares = []
for x in (1, 2, 3, 4):
    squares.append(x * x)
# squares: [1, 4, 9, 16]
print(squares)

squares = [x * x for x in (1, 2, 3, 4)]
print(squares)
# squares: [1, 4, 9, 16]

squares = [x * x for x in range(1, 5)]
print(squares)
# squares: [1, 4, 9, 16]
