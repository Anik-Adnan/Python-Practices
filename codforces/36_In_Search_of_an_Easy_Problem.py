n = int(input())
s = input().split()[:n]
count = 0
for i in s:
    if i == "1":
        break
    else:
        count += 1
if count == len(s):
    print("EASY")
else:
    print("HARD")
