i = 10
f = 1.5
s = "foo"
l = ['a', 1, 2]
d = {'a': 1, 2: 'foo'}

# The following statements are all equivalent
# same output all times
# "10 1.5 foo ['a', 1, 2] {'a': 1, 2: 'foo'}"

print("{} {} {} {} {}".format(i, f, s, l, d))
print(str.format("{} {} {} {} {}", i, f, s, l, d))
print("{0} {1} {2} {3} {4}".format(i, f, s, l, d))
print("{0:d} {1:0.1f} {2} {3!r} {4!r}".format(i, f, s, l, d))
print("{i:d} {f:0.1f} {s} {l!r} {d!r}".format(i=i, f=f, s=s, l=l, d=d))
print(f"{i} {f} {s} {l} {d}")
print(f"{i:d} {f:0.1f} {s} {l!r} {d!r}")

# r reference, Python also supports C-style qualifiers for string formatting.
print("%d %0.1f %s %r %r" % (i, f, s, l, d))
print("%(i)d %(f)0.1f %(s)s %(l)r %(d)r" % dict(i=i, f=f, s=s, l=l, d=d))
