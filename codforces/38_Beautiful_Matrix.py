m = []
t = 1
while t <= 5:
    row = list(map(int, input().split()))
    m.append(row)
    t += 1
for i in range(5):
    for j in range(5):
        if m[i][j] == 1:
            row = i+1
            col = j+1

print(abs(row-3)+abs(col-3))
