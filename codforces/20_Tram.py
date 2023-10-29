t = int(input())
T = 1
passenger = []
while T <= t:
    p = list(map(int, input().split()))
    passenger.append(p)
    T += 1

passenger_list = []
passengers = 0
for i in range(len(passenger)):
    for j in range(2):
        if j == 0:
            passengers -= passenger[i][j]
        elif j == 1:
            passengers += passenger[i][j]

        passenger_list.append(passengers)

print(max(passenger_list))
