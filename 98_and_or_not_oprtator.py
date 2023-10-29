# produces an unexpected result because bool(4) and
# bool(6) each evaluate to True
a = 1
# if a == 3 or 4 or 6: #unexpected result
if a == 3 or a == 4 or a == 6:
    print('yes')
else:
    print('no')

# Using the in operator is the canonical way to write this.
if a in (3, 4, 6):
    print('yes')
else:
    print('no')