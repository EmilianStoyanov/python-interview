colors = ['red', 'green', 'blue', 'red', 'green', 'green']

d = {}
for color in colors:

    if color not in d:
        d[color] = 0
    d[color] += 1

print(d)


# d = {}
# for color in colors:
#     d[color] = d.get(color, 0) + 1
# print(d)

