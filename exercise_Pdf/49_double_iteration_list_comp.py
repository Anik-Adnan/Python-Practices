def foo(i):
    yield i, i + 0.5


for i in range(3):
    for x in foo(i):
        print(str(x))

# This becomes:
[str(x)
    for i in range(3)
 for x in foo(i)
 ]
# This can be compressed into one line as
l = [str(x) for i in range(3) for x in foo(i)]
print(l)
