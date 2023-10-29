# filter without function

# discards 0, [] and ''

print(list(filter(None, [1, 0, 2, [], '', 'a'])))

# equivalent list comprehension
print([i for i in [1, 0, 2, [], '', 'a'] if i])

# equivalent generator expression
print(list((i for i in [1, 0, 2, [], '', 'a'] if i)))

# Out: [1, 2, 'a']
