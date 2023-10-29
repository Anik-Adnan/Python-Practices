# `If v is a variable, the command del v removes the variable from its scope. For example:
x = 5
print(x) # out: 5
del x # x variable removed all scope ,local function scope
# print(x) # NameError: name 'f' is not defined

# del v.name
# This command triggers a call to v.__delattr__(name).
# The intention is to make the attribute name unavailable. For example:
class A:
    pass
a = A()
a.x = 7
print(a.x) # out: 7
del a.x # a.x deleted
# print(a.x) # error: AttributeError: 'A' object has no attribute 'x'

# del v[item]
# This command triggers a call to v.__delitem__(item).
# The intention is that item will not belong in the mapping implemented by the object v. For example:
x = {'a': 1, 'b': 2}
del x['a']
print(x) # out: {'b': 2}
# print(x['a']) # error: KeyError: 'a'

# del v[a:b]
# This actually calls v.__delslice__(a, b).
x = [0, 1, 2, 3, 4]
del x[1:3]
print(x) # out: [0, 3, 4]