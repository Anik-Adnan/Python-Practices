a = [1, 2, 3, 4, 5]

# append method --> appends a new element to the end of the list.
# a.append(7)
# print(a)
# # Append another list
# b = [8, 9]
# a.append(b)
# print(a)
# my_string = "hello world"
# a.append(my_string)
# print(a)


# # extend(enumerable) – extends the list by appending elements from another enumerable.
# a = [1, 2, 3, 4, 5, 6, 7, 7]
# b = [8, 9, 10]
# # Extend list by appending all elements from b
# a.extend(b)
# print(a)  # a: [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10]
# # Extend list with elements from a non-list enumerable:
# a.extend(range(3))
# print(a)  # a: [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10, 0, 1, 2]
# Lists can also be concatenated with the + operator. Note that this does not modify any of the original lists:
# a = [1, 2, 3, 4, 5, 6] + [7, 7] + b
# print(a) # a: [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10]
