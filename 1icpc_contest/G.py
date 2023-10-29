t = int(input())
T = 1
while T <= t:
    n = int(input())
    ks = []
    for i in range(n):
        ks.append(input())
    print(ks)
    s = input()
    max_len = []
    for i in range(len(ks)):
        m = max(ks, key=lambda x: len(x))
        max_len.append(m)
        ks.remove(m)

    count = 0
    c = 0
    l = []
    temp = ""
    Fal = True
    for i in ks:
        if i not in temp:
            temp += s[i]
            s.pygame.sprite.remove()
            c = s.count(i)

    # for i in range(len(s)):
    #     for j in reversed(range(len(s))):
    #         if s[i:j] in ks:
    #             count += 1

    if c == 0:
        print(f"Case {T}: {c}")
    else:
        print(f"Case {T}: impossible")
    T += 1
