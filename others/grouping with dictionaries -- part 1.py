names = ['raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa', 'judith', 'charlie']

d = {}

for name in names:
    key = len(name)
    if key not in d:
        d[key] = []
    d[key].append(name)

print(d)
