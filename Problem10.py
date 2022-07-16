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


def main():
    sieve = list(range(n))
    sieve[1] = 0
    for i in sieve[2:]:
        for j in range(i ** 2, len(sieve), i):
            sieve[j] = 0
    return sieve


if __name__ == '__main__':
    n = 2_000_000
    result = str(sum(main()))
    res = result[-12:-9] + ' ' + result[-9:-6] + ' ' + result[-6:-3] + ' ' + result[-3:]
    print(f'Сумма всех простых чисел ниже {n}'
          f' равна: {res}')
