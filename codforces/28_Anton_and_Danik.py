n = int(input())
g = input()[:n]
count_A = g.count("A")
count_D = g.count("D")
if count_A == count_D:
    print("Friendship")
elif count_A > count_D:
    print("Anton")
else:
    print("Danik")
