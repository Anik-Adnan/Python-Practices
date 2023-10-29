from collections import defaultdict
d = defaultdict(int)
print(d['key'])  # 0
d['key'] = 5
print(d['key'])  # 5

d = defaultdict(lambda: 'empty')
print(d['key'])  # 'empty'
d['key'] = 'full'
print(d['key'])  # 'full'

# ######
d = {}
d.setdefault('Another_key', []).append("This worked!")
print(d)
