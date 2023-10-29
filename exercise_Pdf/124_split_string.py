# str.split(sep=None, maxsplit=-1)

print("This is a sentence.".split())
# ['This', 'is', 'a', 'sentence.']
print(" This is a sentence. ".split())
# ['This', 'is', 'a', 'sentence.']
print(" ".split())
# []

print("Earth,Stars,Sun,Moon".split(','))
# ['Earth', 'Stars', 'Sun', 'Moon']

print(" This is    a    sentence. ".split(' '))
# ['', 'This', 'is', '', '', '', 'a', 'sentence.', '', '']
print("This is a sentence.".split('e'))
# ['This is a s', 'nt', 'nc', '.']
print("This is a sentence.".split('en'))
# ['This is a s', 't', 'ce.']


# The default is to split on every occurrence of the delimiter, however the maxsplit parameter limits the number of
# splittings that occur. The default value of -1 means no limit:

print("This is a sentence.".split('e', maxsplit=0))
# ['This is a sentence.']

print("This is a sentence.".split('e', maxsplit=1))
# ['This is a s', 'ntence.']
print("This is a sentence.".split('e', maxsplit=2))
# ['This is a s', 'nt', 'nce.']
print("This is a sentence.".split('e', maxsplit=-1))
# ['This is a s', 'nt', 'nc', '.']

# str.rsplit(sep=None, maxsplit=-1)
# str.rsplit ("right split") differs from str.split ("left split") when maxsplit is specified. The splitting starts at the
# end of the string rather than at the beginning:

print("This is a sentence.".rsplit('e', maxsplit=1))
# ['This is a sentenc', '.']
print("This is a sentence.".rsplit('e', maxsplit=2))
# ['This is a sent', 'nc', '.']
