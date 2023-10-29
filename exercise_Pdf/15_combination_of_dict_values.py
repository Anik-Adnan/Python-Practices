import itertools
options = {
    "x": ["a", "b"],
    "y": [10, 20, 30]}
keys = options.keys()
values = (options[key] for key in keys)
combinations = [dict(zip(keys, combination))
                for combination in itertools.product(*values)]
print(combinations)

# [{'x': 'a', 'y': 10},
#  {'x': 'a', 'y': 20},
#  {'x': 'a', 'y': 30},
#  {'x': 'b', 'y': 10},
#  {'x': 'b', 'y': 20},
#  {'x': 'b', 'y': 30}]

# d = [dict(zip(key, options[key])) for key in options]
# print(d)
