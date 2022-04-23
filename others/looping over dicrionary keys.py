d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}

# for k in d:
#     print(k)


t = {k: d[k] for k in d if not k.startswith('r')}
print(t)
