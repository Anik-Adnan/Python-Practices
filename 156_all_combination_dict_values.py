import itertools
options = {
    "x": ["a", "b"],
    "y": [10, 20, 30]}

keys = options.keys()
values = list(options[key] for key in keys)
print(list(itertools.product(*values)))
# [('a', 10), ('a', 20), ('a', 30), ('b', 10), ('b', 20), ('b', 30)]

# values = options.values()
# combinations = [dict(zip(keys, combination))
#                 for combination in options.values()]
combinations = [dict(zip(keys, combination))
                for combination in itertools.product(*values)]
print(combinations)
