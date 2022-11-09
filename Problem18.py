
a = [
    [3],
    [7, 4],
    [2, 4, 6],
    [8, 5, 9, 3]
]


def path(elements: ((int, ...), ...), level: int = 0, position: int = 0) -> int:
    if level == len(elements): return 0
    #print(level, elements)
    left, right = path(elements, level + 1, position), path(elements, level + 1, position + 1)
    print(left, right)
    return elements[level][position] + max([left, right])



print(path(a))  # 1074