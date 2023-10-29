# Get a list of uppercase characters from a string
a = [s.upper() for s in "Hello World"]
print(a)
# ['H', 'E', 'L', 'L', 'O', ' ', 'W', 'O', 'R', 'L', 'D']


# Strip off any commas from the end of strings in a list
s = [w.strip(',') for w in ['these,', 'words,,', 'mostly', 'have,commas,']]
print(s)
# ['these', 'words', 'mostly', 'have,commas']


# Organize letters in words more reasonably - in an alphabetical order
sentence = "Beautiful is better than ugly"
sort = ["".join(sorted(word, key=lambda x: x.lower()))
        for word in sentence.split()]
print(sort)
# ['aBefiltuu', 'is', 'beertt', 'ahnt', 'gluy']
