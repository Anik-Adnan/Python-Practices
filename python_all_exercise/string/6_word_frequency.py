import re
from collections import Counter
s = "i am Anik Adnan. Everybody knows Anik Adnan is a good boy."


def word_freq(s):
    s = re.split(' |\.', s)
    freq = {i: s.count(i) for i in s}
    for k, v in freq.items():
        print(f"{k:>10} : {v}")


word_freq(s)


# initializing string
test_str = 'Gfg is best . Geeks are good and Geeks like Gfg'

# printing original string
print("The original string is : " + str(test_str))

# Words Frequency in String Shorthands
# Using Counter() + split()
res = Counter(test_str.split())

# printing result
print("The words frequency : " + str(dict(res)))
