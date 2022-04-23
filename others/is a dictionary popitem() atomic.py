d = {'matthew': 'red', 'rachel': 'green', 'raymond': 'blue'}

while d:
    key, value = d.popitem()
    print(f'{key} ---> {value}')

print(d)
