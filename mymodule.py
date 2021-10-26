# autor: Misac Igor
# licese: GPL3
"""This is the "example" module.

"""


def hello():
    print('Hello, world!')


def fib(n):
    a = b = 1
    print(a, end=', ')
    for i in range(n - 2):
        a, b = b, a + b
        print(a, end=', ')
    return b
