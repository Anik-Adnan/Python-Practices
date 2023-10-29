# Sort by sub dict:
import datetime
l = [{'name': 'John Cena', 'birthday': datetime.date(1992, 9, 12), 'size': {'height': 175,
                                                                            'weight': 100}},
     {'name': 'Chuck Norris', 'birthday': datetime.date(1990, 8, 28), 'size': {'height': 180,
                                                                               'weight': 90}},
     {'name': 'Jon Skeet', 'birthday': datetime.date(1991, 7, 6), 'size': {'height': 185,
                                                                           'weight': 110}}]
l.sort(key=lambda item: item['size']['height'])
print(l)
# l: [John Cena, Chuck Norris, Jon Skeet]
