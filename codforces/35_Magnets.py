n = int(input())
count = 0
t = 1
l = []
while t <= n:
    s = input()
    l.append(s)
    t += 1

for i in range(len(l)-1):
    if l[i] != l[i + 1]:
        count += 1
print(count+1)
