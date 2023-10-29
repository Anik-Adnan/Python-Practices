# list sort() method
name = ['a', 'Anik', 'asif', 'rahid', 'momotuz', 'b']
name.sort()
print(name)

# tuple sorted function
# return always list because tuple immutable
name2 = ('a', 'Anik', 'asif', 'rahid', 'momotuz', 'b')
print(sorted(name2))
# print(name2)  # not changed because immutable

# set immutable, order
name3 = {'a', 'Anik', 'asif', 'rahid', 'momotuz', 'b'}
print(sorted(name3))
print(name3)  # not changed because immutable, unorder

guiters = [
    {'model': 'yamaha', 'price': 8400},
    {'model': 'faith naptune', 'price': 50000},
    {'model': 'faith apallo venus', 'price': 35000},
    {'model': 'taylor 814ce', 'price': 450000},
]
print(sorted(guiters, key=lambda d: d['price']))
print(sorted(guiters, key=lambda d: d['price'], reverse=True))
