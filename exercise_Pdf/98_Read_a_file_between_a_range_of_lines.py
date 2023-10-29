import itertools
with open('myfile1.text', 'r') as f:
    for line in itertools.islice(f, 1, 4):
        # do something here
        print(line, end='')
# I think you are well
# I am also well
# what r u doing??
