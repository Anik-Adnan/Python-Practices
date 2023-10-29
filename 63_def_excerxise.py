def square_list(n):
    square=[]
    for i in n:
        square.append(i**2)
    return square

number=list(range(1,11))
print(square_list(number))

