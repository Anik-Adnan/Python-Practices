t = int(input())
T = 1
while T <= t:
    w = input()
    if len(w) <= 10:
        print(w)
    else:
        print(f"{w[0]}{len(w)-2}{w[-1]}")
    T += 1
