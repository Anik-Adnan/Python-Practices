
a = ['one', 'two', 'three', 'four']
l = []
for i in a:
    l.append(i.upper())
print(l)

x = list(map(lambda e: e.upper(), ['one', 'two', 'three', 'four']))
print(x)
