y = int(input())
for i in range(y + 1, 9000 + 50):
    temp = ""
    for j in str(i):
        if j not in temp:
            temp += j
    if temp == str(i):
        print(temp)
        break
