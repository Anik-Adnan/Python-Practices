n = int(input())
t = 1
while t <= n:
    num = int(input())
    s = input()[:num]
    tt = s.count("T")
    m = s.count("M")
    while s.find("TMT") == None:
        index = s.find("TMT")
        del s[index:index+3]
        # s = s.replace(s[indes:index+3], "")
    if len(s) == 0:
        print("YES")
    else:
        print("NO")
    print(s)
    t += 1
