n = int(input())
p = "NO"
lucy_num = []
for j in range(1, 1000):
    for i in str(j):
        if i == "4" or i == "7":
            devide = 1
        else:
            devide = 0
            break
    if devide == 1:
        lucy_num.append(j)

for i in lucy_num:
    if n % i == 0:
        p = "YES"

print(p)
