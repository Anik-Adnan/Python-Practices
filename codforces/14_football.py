f = input()
count = 0
for i in range(len(f) - 1):
    if f[i] == f[i + 1]:
        count += 1
    else:
        count = 0
    if count >= 6:
        p = "YES"
        break
    else:
        p = "NO"
print(p)
