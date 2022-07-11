def compute(n):
    a = b = c = d = 0
    n1 = int(n/10)
    for i in range(n1, n):
        for j in range(n1, n):
            proizv = i * j
           #perev = reversed1(str(proizv))
            if str(i * j) == str(i * j)[ : : -1] and a < (i * j):
                a, b, c, d = (i * j), str(i * j)[ : : -1], i, j
    print(f"Самый большой палиндром при умножении {len(str(n1))}-значных чисел: {c} x {d} равняется значению {a}, '<-->', {b}")

if __name__ == "__main__":
    compute(1000)

# def compute():
#     ans = max(i * j for i in range(100, 1000) for j in range(100, 1000) if str(i * j) == str(i * j)[ : : -1])
#     return str(ans)
#
#
# if __name__ == "__main__":
#     print(compute())