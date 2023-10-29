test_list = [12, 67, 98, 34]
result = []
for i in test_list:
    sum = 0
    for j in str(i):
        sum += int(j)
    result.append(sum)
print("real list : ", test_list)
print("sum of number list : ", result)

# n = list(map(lambda i: sum(int(j) for j in str(i)), test_list))
# print(n)
