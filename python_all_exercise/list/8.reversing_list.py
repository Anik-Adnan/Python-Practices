# Reversing a list using reversed()
def Reverse(lst):
    return [ele for ele in reversed(lst)]


# Driver Code
l = [10, 11, 12, 13, 14, 15]
print(Reverse(l))
l2 = reversed(l)  # iterator
print(*l2)

l.reverse()
print(l)
l = [1, 2, 3, 4]
print(l[::-1])
