numbers = input(int()).split(',')
target = int(input())
res = []
i = 0
while int(numbers[i]) + int(numbers[i + 1]) != target:
    res = res.append(numbers[i])
    res = res.append(numbers[i+1]
    i=i+1
print(res)
