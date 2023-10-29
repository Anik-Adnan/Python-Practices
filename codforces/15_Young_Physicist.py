t = int(input())
sum_X = 0
sum_Y = 0
sum_Z = 0
T = 1
while T <= t:
    x, y, z = map(int, input().split())
    sum_X += x
    sum_Y += y
    sum_Z += z
    T += 1

if sum_X == sum_Z == sum_Y == 0:
    print("YES")
else:
    print("NO")
