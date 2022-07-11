from time import perf_counter

x1, x2, a = 3, 5, 1000


def fib():
    ans = sum(x for x in range(a) if (x % x1 == 0 or x % x2 == 0))
    return ans


start = perf_counter()
print(f"Сумма всех чисел кратных {x1} и {x2} из {a} равнa: {fib()}")
end = perf_counter()
print(f"Время выполнения функции составило: {end - start:.9f}")
