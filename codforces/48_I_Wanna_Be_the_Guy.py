l = int(input())
x = list(map(int, input().split()))
x = x[1:]
y = list(map(int, input().split()))
y = y[1:]
level = list(range(1, l + 1))
level_up = x + y
level_up = list(set(level_up))
level_up.sort()
if level == level_up:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
