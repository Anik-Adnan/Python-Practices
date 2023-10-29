# Write a program that accepts a sequence of whitespace separated words as input and prints
#  the words after removing all duplicate words and sorting them alphanumerically.
# input
# hello world and practice makes perfect and hello world again
# output
# again and hello makes perfect practice world

s = input()
words = [word for word in s.split(" ")]
print(" ".join(sorted(list(set(words)))))


# or
# s = input().split()
# print(" ".join(sorted(list(set(s)))))

# or
word = sorted(list(set(input().split())))
print(" ".join(word))

# same

# word = input().split()

# for i in word:
#     if word.count(i) > 1:    #count function returns total repeatation of an element that is send as argument
#         word.remove(i)     # removes exactly one element per call

# word.sort()
# print(" ".join(word))


# or
# word = input().split()
# # removal operation with comprehension method
# [word.remove(i) for i in word if word.count(i) > 1]
# word.sort()
# print(" ".join(word))


# or
# inp_string = input("Enter string: ").split()
# out_string = []
# for words in inp_string:
#     if words not in out_string:
#         out_string.append(words)
# print(" ".join(sorted(out_string)))
