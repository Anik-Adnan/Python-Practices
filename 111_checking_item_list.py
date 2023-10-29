lst = ['test', 'twest', 'tweast', 'treast']
print('test' in lst)
# Out: True
print('toast' in lst )
# Out: False

slst = set(lst)
print( 'test' in slst )
# Out: True