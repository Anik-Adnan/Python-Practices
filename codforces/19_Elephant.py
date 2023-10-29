a = int(input())
step = (5, 4, 3, 2, 1)
step_count = 0
for i in step:
    if a % i == 0:
        step_count += a // i
        break
    elif a % i > 0:
        step_count += a // i
        a = a % i
print(step_count)
