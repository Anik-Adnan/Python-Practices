s = input()
w = "hello"
j = 0
p = "NO"
for i in range(len(s)):
    if s[i] == w[j]:
        j += 1
    if j >= 5:
        p = "YES"
        break
print(p)
