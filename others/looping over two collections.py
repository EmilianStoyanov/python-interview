names = ['ivo', 'rachel', 'maya']
colors = ['red', 'green', 'blue', 'yellow']

n = min(len(names), len(colors))
for i in range(n):
    print(names[i], '-->', colors[i])

print('---1----')

for name, color in zip(names, colors):
    print(name, '-->', color)

