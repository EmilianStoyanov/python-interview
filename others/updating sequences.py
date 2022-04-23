# names = ['ivo', 'rachel', 'maya', 'betty', 'melissa', 'charlie']
#
# del names[0]
# names.pop(0)
# names.insert(0, 'mark')
#
# print(names)
from collections import deque

names = deque(['ivo', 'rachel', 'maya', 'betty', 'melissa', 'charlie'])
del names[0]
names.popleft()
names.appendleft('mark')

save = ''
for name in list(names):
    save += name + '  '

print(save.rstrip())
