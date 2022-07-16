# n = int(input("Введите верхнюю границу диапазона: "))
# sieve = set(range(2, n + 1))
# summ = 0
#
# while sieve:
#     prime = min(sieve)
#     # print(prime, end = "\t")
#
#     sieve -= set(range(prime, n + 1, prime))
#     summ = summ + prime
# print(f'Сумма всех простых чисел ниже {n} равна {summ}')

def eratosthen(n):
    sieve = list(range(n))
    sieve[1] = 0
    for i in sieve[2:]:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return sieve
n = 2_000_000
print(f'Сумма всех простых чисел ниже {n} равна {sum(eratosthen(n))}')
