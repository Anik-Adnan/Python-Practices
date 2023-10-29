from datetime import datetime, timedelta
t = (12, 45, 22222, 103, 6)
print('{0} {2} {1} {2} {3} {2} {4} {2}'.format(*t))
# Out: 12 22222 45 22222 103 22222 6 22222

# As format is a function, it can be used as an argument in other functions:
number_list = [12, 45, 78]
print(list(map('the number is {}'.format, number_list)))
# Out: ['the number is 12', 'the number is 45', 'the number is 78']


once_upon_a_time = datetime(2010, 7, 1, 12, 0, 0)
delta = timedelta(days=13, hours=8, minutes=20)
gen = (once_upon_a_time + x * delta for x in range(5))
print('\n'.join(map('{:%Y-%m-%d %H:%M:%S}'.format, gen)))
# Out: 2010-07-01 12:00:00
# 2010-07-14 20:20:00
# 2010-07-28 04:40:00
# 2010-08-10 13:00:00
# 2010-08-23 21:20:00
