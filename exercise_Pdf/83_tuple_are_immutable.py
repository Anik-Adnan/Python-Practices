# One of the main differences between lists and tuples in Python is that tuples are immutable, that is, one cannot
# add or modify items once the tuple is initialized.

t = (1, 4, 9)
#t[0] = 2
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment


# Similarly, tuples don't have .append and .extend methods as list does. Using += is possible, but it changes the
# binding of the variable, and not the tuple itself:
t = (1, 2)
q = t
t += (3, 4)
print(t)  # (1, 2, 3, 4)
print(q)  # (1, 2)
# You can use the += operator to "append" to a tuple - this works by creating a new tuple with the new element you
# "appended" and assign it to its current variable; the old tuple is not changed, but replaced!


# Be careful when placing mutable objects, such as lists, inside tuples. This may lead to very confusing outcomes
# when changing them. For example:
t = (1, 2, 3, [1, 2, 3])
#t[3] += [4, 5]

# Will both raise an error and change the contents of the list within the tuple:
# TypeError: 'tuple' object does not support item assignment
print(t)  # (1, 2, 3, [1, 2, 3, 4, 5])
