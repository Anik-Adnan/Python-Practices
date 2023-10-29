d = dict()  # empty dict
print(d)
d = dict(key='value')  # explicit keyword arguments
print(d)
d = dict([('key', 'value')])  # passing in a list of key/value pairs
print(d)
# make a shallow copy of another dict (only possible if keys are only strings!)
# d = dict(**otherdict)
