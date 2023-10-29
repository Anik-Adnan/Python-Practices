# Any class can configure its own string formatting syntax through the __format__ method. A type in the standard
# Python library that makes handy use of this is the datetime type, where one can use strftime-like formatting
# codes directly within str.format:
from datetime import datetime
print(
    'Bangladesh: {dt:%m/%d/%Y}. ISO: {dt:%Y-%m-%d}.'.format(dt=datetime.now()))
# Bangladesh: 07/15/2020. ISO: 2020-07-15.
d = datetime.now()
print(f'{d:%d-%m-%Y}')
