colors = ['red', 'green', 'blue', 'yellow']


def compare_length(c1, c2):
    if len(c1) < len(c2):
        return -1

    if len(c1) > len(c2):
        return 1

    return 0


print(sorted(colors, key=len))
