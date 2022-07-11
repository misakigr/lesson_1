iskom_num, count = 600851475143, 2
num, a = iskom_num, count

print('Делит_1, Делит_2')
while 1:
    if num % count == 0:
        num /= count
        print(count,"*****", int(num))
        if a < num:
            a = num
        if num == 1:
            print(f'Наибольший простой делитель числа {iskom_num}: {int(count)}')
            break
    else:
        count += 1
