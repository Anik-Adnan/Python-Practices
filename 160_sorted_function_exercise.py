guiters = [
    {'model': 'yamaha', 'price': 8400},
    {'model': 'faith naptune', 'price': 50000},
    {'model': 'faith apallo venus', 'price': 35000},
    {'model': 'taylor 814ce', 'price': 450000},
]
print(sorted(guiters, key=lambda d: d['price']))
print()
# samebut reverse order
print(sorted(guiters, key=lambda d: d['price'], reverse=True))

# reversed_list = sorted(guiters, key=lambda d: d['price'], reverse=True)
# print(reversed_list)
