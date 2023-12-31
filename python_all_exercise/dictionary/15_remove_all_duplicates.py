from collections import Counter


def remov_duplicates(input):

    # split input string separated by space
    input = input.split(" ")

    UniqW = Counter(input)

    # joins two adjacent elements in iterable way
    s = " ".join(UniqW.keys())
    print(s)


# Driver program
if __name__ == "__main__":
    input = 'Python is great and Java is also great'
    print(input)
    remov_duplicates(input)


# 22222
# Program without using any external library
s = "Python is great and Java is also great"
l = s.split()
k = []
for i in l:

    # If condition is used to store unique string
    # in another list 'k'
    if (s.count(i) > 1 and (i not in k) or s.count(i) == 1):
        k.append(i)
print(' '.join(k))
