# The default assignment "=" assigns a reference of the original list to the new name. That is, the original name
# and new name are both pointing to the same list object. Changes made through any of them will be reflected
# in another. This is often not what you intended.

import copy
a = [1, 2, 3, 4, 5]
b = a
a.append(6)
print(b)
# b: [1, 2, 3, 4, 5, 6]

# If you want to create a copy of the list you have below options.
# You can slice it:
# new_list = old_list[:]

# You can use the built in list() function:
# new_list = list(old_list)

old_list = [1, 2, 3, 4]
# You can use generic copy.copy():
# inserts references to the objects found in the original.
new_list = copy.copy(old_list)
# This is a little slower than list() because it has to find out the datatype of old_list first.

# If the list contains objects and you want to copy them as well, use generic copy.deepcopy():
# inserts copies of the objects found in the original.
new_list = copy.deepcopy(old_list)
# Obviously the slowest and most memory-needing method, but sometimes unavoidable.
