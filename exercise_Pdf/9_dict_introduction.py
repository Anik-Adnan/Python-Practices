# literal syntax
d = {}
d = {'key': 'value'}
# d = {**otherdict}  # makes a shallow copy of otherdict
# also updates the shallow copy with the contents of the yetanotherdict.
# d = {**otherdict, **yetotherdict}


# dict comprehension
d = [('key', 'value')]
print(type(d))
dc = {k: v for k, v in d}
print(dc)

# bilt-in class:dict()
d = dict()  # empty dict
d = dict(key1='value1', key2='value2')  # explicit keyword arguments
print(d)
# passing in a list of key/value pairs
d = dict([('key0', 'value0'), ('key1', 'value1')])
print(d)
# make a shallow copy of another dict (only possible if keys are only strings!)
#d = dict(**otherdict)


# modifying a dict
# To add items to a dictionary, simply create a new key with a value
# It also possible to add list and dictionary as value
d['newkey'] = 10
d['new_list'] = [10, 20, 30]
d['new_dict'] = {'nested_dict': 1}

# to delete an item
del d['newkey']
