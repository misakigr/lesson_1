# рекурсия, цикл for или мемоизация?

memory = {(1, 0): 1, (0, 1): 1}


def func(x, y):
    if (x, y) not in memory:
        if x == 0:
            memory[(x, y)] = func(x, y - 1)
            # print(memory[(x, y)])
        elif y == 0:
            memory[(x, y)] = func(x - 1, y)
            # print(memory[(x, y)])
        else:
            memory[(x, y)] = func(x - 1, y) + func(x, y - 1)
            # print(memory[(x, y)])
    return memory[(x, y)]


print(func(2, 2))
print(func(20, 20))
