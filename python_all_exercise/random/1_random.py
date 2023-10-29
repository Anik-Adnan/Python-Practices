import random

r = random.randint(1, 4)  # int random number
print(r)

r = random.random()  # floating random number
print(r)

r = random.randrange(5, 10, 3)  # intiger random number
print(r)

r = random.uniform(5, 10)  # float random number
print(r)

# returning 5 element in a list between 1-20
r = random.sample(range(1, 20), 5)
print(r)

random.shuffle(r)
print(r)  # shuffle list

ch = random.choice(r)
print(ch)
