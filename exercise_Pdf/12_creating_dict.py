# Creating and populating it with values
stock = {'eggs': 5, 'milk': 2}

# Or creating an empty dictionary
dictionary = {}
# And populating it after
dictionary['eggs'] = 5
dictionary['milk'] = 2

# Values can also be lists
mydict = {'a': [1, 2, 3], 'b': ['one', 'two', 'three']}
# Use list.append() method to add new elements to the values list
mydict['a'].append(4)  # => {'a': [1, 2, 3, 4], 'b': ['one', 'two', 'three']}
# => {'a': [1, 2, 3, 4], 'b': ['one', 'two', 'three', 'four']}
mydict['b'].append('four')

# We can also create a dictionary using a list of two-items tuples
iterable = [('eggs', 5), ('milk', 2)]
dictionary = dict(iterable)

# Or using keyword argument:
dictionary = dict(eggs=5, milk=2)

# Another way will be to use the dict.fromkeys:
dictionary = dict.fromkeys(('milk', 'eggs'), (2, 5))
# {'milk': None, 'eggs': None}
dictionary = dict.fromkeys(('milk', 'eggs'))
# {'milk': 2, 'eggs': 5}
