t = int(input())
x = 0
T = 1
while T <= t:
    bit = input()
    if bit == "X++" or bit == "++X":
        x += 1
    elif bit in "X----X":
        x -= 1
    T += 1
print(x)
