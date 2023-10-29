# using for loop
n = int(input())
square = {}
for i in range(1, n + 1):
    square[i] = i*i
print(square)

# using dict comprehension
print({i: i**2 for i in range(1, n+1)})


num = int(input("Number: "))
print(dict(list(enumerate((i * i for i in range(num+1))))))
