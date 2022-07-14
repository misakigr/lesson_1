n = int(input("Введите верхнюю границу диапазона: "))
b = int(input("Введите мах порядковый номер желаемого числа: "))
sieve = set(range(2, n+1))
c = 1
while sieve:
    prime = min(sieve)
    #print(prime, end = "\t")
    print(c, prime)
    sieve -= set(range(prime, n+1, prime))
    if c == b:
        break
    c += 1

