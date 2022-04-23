colors = ['red', 'green', 'blue', 'yellow']

for i in range(len(colors)):
    print(f'{i}--->P{colors[i]}')

print('---1----')

for i, color in enumerate(colors):
    print(f'{i}--->P{colors[i]}')
