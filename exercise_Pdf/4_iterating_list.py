lst = ['alpha', 'bravo', 'charlie', 'delta', 'echo']

# for s in lst:
#     print(s[:1])  # print the first letter


for idx, s in enumerate(lst):
    print("%s has an index of %d" % (s, idx))
print('###')

for i in range(2, 4):
    print("lst at %d contains %s" % (i, lst[i]))

# for s in lst[1::2]:
#     print(s)
# # bravo
# # delta

# for i in range(1, len(lst), 2):
#     print(lst[i])
# # bravo
# # delta
