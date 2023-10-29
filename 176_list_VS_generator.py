# list vs generator
# memory usage, time
# when to use list , when use generator
import time
t1 = time.time()
# l = [i ** 2 for i in range(1000000)]
l = (i ** 2 for i in range(1000000))
print(time.time()-t1)
