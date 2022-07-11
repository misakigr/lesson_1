a = b = 1
sumchet, maxchislo = 0, 4_000_000

print("0,", a, end=', ')

while b < maxchislo:
    a, b = b, a + b
    print(a, end=', ')
    if a%2 == 0:
        sumchet += a
print()
print(f'Сумма всех четных чисел из ряда Фибоначчи не превышающих {maxchislo} равна: {sumchet}')