# input
# Hello world
# Practice makes perfect

# output
# HELLO WORLD
# PRACTICE MAKES PERFECT

lst = []

while True:
    x = input()
    if len(x) == 0:
        break
    lst.append(x.upper())

for line in lst:
    print(line)


# or

# lines = []
# while True:
#     s = raw_input()
#     if s:
#         lines.append(s.upper())
#     else:
#         break

# for sentence in lines:
#     print sentence

# or

# def user_input():
#     while True:
#         s = input()
#         if not s:
#             return
#         yield s


# for line in map(str.upper, user_input()):
#     print(line)
