# Remove duplicate values in list
names = ["aixk", "duke", "edik", "tofp", "duke"]
print(list(set(names))) 
# Out: ['duke', 'tofp', 'aixk', 'edik']

# by converting a list to a set the original ordering is lost.

# To preserve the order of the list use an OrderedDict
import collections
print( collections.OrderedDict.fromkeys(names).keys())
# Out: ['aixk', 'duke', 'edik', 'tofp']