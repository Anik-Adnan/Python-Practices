s = "anik adnan"


def dup_char(s):
    ss = set()
    for i in s:
        if s.count(i) > 1:
            ss.add(i)
    return ss


print(dup_char(s))
