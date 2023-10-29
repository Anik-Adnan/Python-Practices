# To find the largest items in a collection, heapq module has a function called nlargest, we pass it two arguments, the
# first one is the number of items that we want to retrieve, the second one is the collection name:

import heapq

numbers = [1, 4, 2, 100, 20, 50, 32, 200, 150, 8]
print(heapq.nlargest(4, numbers))
# [200, 150, 100, 50]


# Similarly, to find the smallest items in a collection, we use nsmallest function:
print(heapq.nsmallest(4, numbers))
# [1, 2, 4, 8]
