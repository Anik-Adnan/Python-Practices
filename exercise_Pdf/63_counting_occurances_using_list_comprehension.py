# Count the numbers in `range(1000)` that are even and contain the digit `9`:
print(sum(
    1 for x in range(1000)
    if x % 2 == 0 and
    '9' in str(x)
))
# Out: 95
print(sum(1 for i in range(11) if i % 2 == 0))

# The basic concept can be summarized as:
# 1. Iterate over the elements in range(1000).
# 2. Concatenate all the needed if conditions.
# 3. Use 1 as expression to return a 1 for each item that meets the conditions.
# 4. Sum up all the 1s to determine number of items that meet the conditions.

# Note: Here we are not collecting the 1s in a list (note the absence of square brackets), but we are passing the ones
# directly to the sum function that is summing them up. This is called a generator expression, which is similar to a
# Comprehension
