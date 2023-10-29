dict1 = {'w': 1, 'x': 1}
dict2 = {'x': 2, 'y': 2, 'z': 2}

print({k: v for d in [dict1, dict2] for k, v in d.items()})
# Out: {'w': 1, 'x': 2, 'y': 2, 'z': 2}

# However, dictionary unpacking (PEP 448) may be a preferred.

# Python 3.x Version ≥ 3.5
print({**dict1, **dict2})
# Out: {'w': 1, 'x': 2, 'y': 2, 'z': 2}
