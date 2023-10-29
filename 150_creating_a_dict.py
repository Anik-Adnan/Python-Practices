dictionary = {}
stock = {'eggs': 5, 'milk': 2}
print(stock)

dictionary['pen'] = 10
dictionary['pencil'] = 15
print(dictionary)

mydict = {'a': [1, 3, 4], 'b': ['one', 'two', 'three']}
mydict['a'].append(8)
print(mydict)
mydict['b'].append('five')
print(mydict)

# We can also create a dictionary using a list of two-items tuples
iterable = [('eggs', 5), ('milk', 2)]
dictionary = dict(iterable)
print(dictionary)

# Or using keyword argument:
dictionary = dict(eggs=5, milk=2)
print(dictionary)

# Another way will be to use the dict.fromkeys:
dictionary = dict.fromkeys(('milk', 'eggs'))  # => {'milk': None, 'eggs': None}
print(dictionary)
# => {'milk': 2, 'eggs': 5}
dictionary = dict.fromkeys(('milk', 'eggs'), (2, 5))
print(dictionary)
