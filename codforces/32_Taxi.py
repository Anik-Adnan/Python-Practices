import math
n = int(input())
passengers = list(map(int, input().split()))
passengers.sort()
count_1 = passengers.count(1)
count_2 = passengers.count(2)
count_3 = passengers.count(3)
count_4 = passengers.count(4)

car_count = count_4 + (count_2 // 2)
if count_2 % 2 == 1:
    if count_1 <= 2:
        count_1 -= count_1
        car_count += 1
    else:
        count_1 -= 2
        car_count += 1


if count_1 < count_3:

    c = count_1+(count_3-count_1)
    car_count += c
elif count_1 > count_3:
    count_1 = math.ceil((count_1-count_3)/4)
    c = count_3 + count_1
    car_count += c
else:
    car_count += count_1
print(car_count)
