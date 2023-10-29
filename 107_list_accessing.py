lst = [1, 2, 3, 4]
# lst[start:end:step]
print(len(lst))
print(lst[1:] )  # [2, 3, 4]
print(lst[:3] ) # [1, 2, 3]
print(lst[::2] ) # [1, 3]
print(lst[::-1] ) # [4, 3, 2, 1]
print(lst[-1:0:-1] ) # [4, 3, 2]
print(lst[5:8]) # [] since starting index is greater than length of lst, returns empty list
print(lst[1 :10]) # [2, 3, 4] same as omitting ending index
