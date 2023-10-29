import collections
names = ["aixk", "duke", "edik", "tofp", "duke"]
print(list(set(names)))
# Out: ['duke', 'tofp', 'aixk', 'edik']

# Note that by converting a list to a set the original ordering is lost.


# To preserve the order of the list one can use an OrderedDict
print(collections.OrderedDict.fromkeys(names).keys())
# Out: ['aixk', 'duke', 'edik', 'tofp']
