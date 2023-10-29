# The most interesting property of a heap is that its
#  smallest element is always the first element: heap[0]

import heapq

numbers = [10, 4, 2, 100, 20, 50, 32, 200, 150, 8]
heapq.heapify(numbers)
print(numbers)
# Output: [2, 4, 10, 100, 8, 50, 32, 200, 150, 20]

heapq.heappop(numbers)  # 2
print(numbers)
# Output: [4, 8, 10, 100, 20, 50, 32, 200, 150]


heapq.heappop(numbers)  # 4
print(numbers)
# Output: [8, 20, 10, 100, 150, 50, 32, 200]

heapq.heappop(numbers)  # 4
print(numbers)
# Output: [8, 20, 10, 100, 150, 50, 32, 200]
