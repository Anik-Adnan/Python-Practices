# Reverse elements within a tuple

colors = "red", "green", "blue"
rev = colors[::-1]
print(rev)  # rev: ("blue", "green", "red")
colors = rev
# colors: ("blue", "green", "red")


# Or using reversed (reversed gives an iterable which is converted to a tuple):
rev = tuple(reversed(colors))
print(rev)  # rev: ("blue", "green", "red")
colors = rev
# colors: ("blue", "green", "red")
