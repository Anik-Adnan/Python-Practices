# One method is available for counting the number of occurrences of a sub-string in another string, str.count.
# str.count(sub[, start[, end]])

# str.count returns an int indicating the number of non-overlapping occurrences of the sub-string sub in another
# string. The optional arguments start and end indicate the beginning and the end in which the search will take
# place. By default start = 0 and end = len(str) meaning the whole string will be searched:

s = "She sells seashells by the seashore."
print(s.count("sh"))  # 2
print(s.count("se"))  # 3
print(s.count("sea"))  # 2
print(s.count("seashells"))  # 1

# By specifying a different value for start, end we can get a more localized search and count, for example, if start is
# equal to 13 the call to:
print(s.count("sea", 12))  # 1

# is equivalent to:
t = s[:]
print(t.count("sea"))
# 1
