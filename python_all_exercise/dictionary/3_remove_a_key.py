d = {"a": 1, "b": 2, "c": 3, "d": 4}
del d['d']
d.pop('c')
print(d)
new_dict = {key: val for key, val in d.items() if key != 'b'}
print(new_dict)
