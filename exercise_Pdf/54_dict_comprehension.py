d = {x: x * x for x in (1, 2, 3, 4)}
print(d)  # Out: {1: 1, 2: 4, 3: 9, 4: 16}

# which is just another way of writing:
print(dict((x, x * x) for x in (1, 2, 3, 4)))
# Out: {1: 1, 2: 4, 3: 9, 4: 16}

name_len = {name: len(name)
            for name in ('Stack', 'Overflow', 'Exchange') if len(name) > 6}
print(name_len)  # Out: {'Exchange': 8, 'Overflow': 8}

# rewritten using a generator expression
dict((name, len(name))
     for name in ('Stack', 'Overflow', 'Exchange') if len(name) > 6)
# Out: {'Exchange': 8, 'Overflow': 8}


initial_dict = {'x': 1, 'y': 2}
print({key: value for key, value in initial_dict.items() if key == 'x'})
# Out: {'x': 1}
