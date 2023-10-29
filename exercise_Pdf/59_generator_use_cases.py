
# Generator expressions are lazily evaluated, which means that they generate and return each value only when the
# generator is iterated. This is often useful when iterating through large datasets, avoiding the need to create a
# duplicate of the dataset in memory:

for square in (x ** 2 for x in range(1000000)):
    print(square, end=',')
    # do something

# Another common use case is to avoid iterating over an entire iterable if doing so is not necessary. In this example,
# an item is retrieved from a remote API with each iteration of get_objects(). Thousands of objects may exist, must
# be retrieved one-by-one, and we only need to know if an object matching a pattern exists. By using a generator
# expression, when we encounter an object matching the pattern.
# def get_objects():
# """Gets objects from an API one by one"""
# while True:
# yield get_next_item()
# def object_matches_pattern(obj):
# # perform potentially complex calculation
# return matches_pattern
# def right_item_exists():
# items = (object_matched_pattern(each) for each in get_objects())
# for item in items:
# if item.is_the_right_one:
# return True
# return False
