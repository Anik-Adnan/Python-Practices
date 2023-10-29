# [ <expression> for <element> in <iterable> ]
# There's also an optional 'if' condition:
# [ <expression> for <element> in <iterable> if <condition> ]


# squares = []
# for x in (1, 2, 3, 4):
#     squares.append(x * x)
# print(squares)

squares = [x * x for x in range(1,5) ]
print(squares)

# Get a list of uppercase characters from a string
a=['anik','adnan','biswas']
u = [s[0].upper() for s in a]
print(u)
# ['A', 'A', 'B']

# Strip off any commas from the end of strings in a list
c = [w.strip(',') for w in ['these,', 'words,,', 'mostly', 'have,commas,']]
print(c)
# ['these', 'words', 'mostly', 'have,commas']

# Organize letters in words more reasonably - in an alphabetical order
sentence = "Beautiful is better than ugly"
a= ["".join(sorted(word, key = lambda x: x.lower())) for word in sentence.split()]
print(a)
# ['aBefiltuu', 'is', 'beertt', 'ahnt', 'gluy']