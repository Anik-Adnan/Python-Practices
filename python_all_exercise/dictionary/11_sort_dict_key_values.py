test_dict = {'gfg': [7, 6, 3],
             'is': [2, 10, 3],
             'best': [19, 4]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Sort Dictionary key and values List
# Using loop + dictionary comprehension
res = dict()
for key in sorted(test_dict):
    res[key] = sorted(test_dict[key])

# printing result
print("The sorted dictionary : " + str(res))


# 222
test_dict = {'gfg': [7, 6, 3],
             'is': [2, 10, 3],
             'best': [19, 4]}
res = {key: sorted(test_dict[key]) for key in sorted(test_dict)}

# printing result
print("The sorted dictionary : " + str(res))
