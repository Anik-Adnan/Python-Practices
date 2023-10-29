def is_symmetric(s):
    length = len(s)
    if length % 2:
        mid = length // 2 + 1
    else:
        mid = length // 2
    start1 = 0
    start2 = mid
    fig = 1
    while start1 < mid and start2 < length:
        if s[start1] == s[start2]:
            start1 += 1
            start2 += 1
        else:
            fig = 0
            break

    if fig == 0:
        print("not symmetric")
    else:
        print("symmetric")


s = "mam"
is_symmetric(s)


def is_symmetric2(s):
    length = len(s)
    if length % 2:
        mid = length // 2 + 1
    else:
        mid = length // 2
    if s[:mid] == s[mid:]:
        print("symmetric")
    else:
        print("not symmetric")


s = "mam"
is_symmetric(s)
