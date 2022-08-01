
# while sieve:
#     prime = min(sieve)
#     #print(prime, end = "\t")
#     print(c, prime)
#     sieve -= set(range(prime, n+1, prime))
#     if c == b:
#         break
#     c += 1

c = 1
nacealo = 2
n = int(input("Введите верхнюю границу диапазона: "))
b = int(input("Введите мах порядковый номер желаемого числа: "))
sieve = set(range(nacealo, n+1))

def sie(sieve, c):
    while sieve:
        prime = min(sieve)
        #print(prime, end = "\t")
        print(c, prime)
        sieve -= set(range(prime, n+1, prime))
        if c == b:
            break
        c += 1

sie(sieve, c)