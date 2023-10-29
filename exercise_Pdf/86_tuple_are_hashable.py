# hash((1, 2))  # ok
# hash(([], {"hello"})  # not ok, since lists and sets are not hashabe
# # Thus a tuple can be put inside a set or as a key in a dict only if each of its elements can.
# {(1, 2,)}  # ok
# {([], {"hello"})}  # not ok
