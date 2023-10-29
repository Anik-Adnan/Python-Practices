def Convert(tup, di):
    for a, b in tup:
        di.setdefault(a, []).append(b)
    return di


def convert2(tup):
    d = dict(tup)
    return d


# Driver Code
tups = [("akash", 10), ("gaurav", 12), ("anand", 14),
        ("suraj", 20), ("akhil", 25), ("ashish", 30)]
dictionary = {}
print(Convert(tups, dictionary))

print(convert2(tups))
