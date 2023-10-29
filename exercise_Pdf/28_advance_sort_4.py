# Better way to sort using attrgetter and itemgetterfrom operator import itemgetter,attrgetter
from operator import itemgetter, attrgetter
people = [{'name': 'Anik', 'age': 20, 'salary': 2000},
          {'name': 'Asif', 'age': 18, 'salary': 5000},
          {'name': 'Farhad', 'age': 30, 'salary': 3000}]

by_age = itemgetter('age')
by_salary = itemgetter('salary')
people.sort(key=by_age)
# print(people)  # in-place sorting by age

people.sort(key=by_salary)  # in-place sorting by salary
# print(people)

# itemgetter can also be given an index. This is helpful if you want to sort based on indices of a tuple.
list_of_tuples = [(1, 2), (3, 4), (5, 0), (7, 9), (1, 1)]
list_of_tuples.sort(key=itemgetter(1))
print(list_of_tuples)  # [(5, 0), (1, 2), (3, 4)]
