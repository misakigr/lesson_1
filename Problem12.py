j= 1
n=0
while 1:
    n = j + n
    j = j + 1
    print(n, end="\r")

    razl = []
    k = 0
    for i in range(n + 1):
        if i > 0 and n % i == 0:
            razl.append(int(n / (n / i)))
            k += 1
    if k >= 37:
        print(n, "(",k,"делител. )", ":", razl)
        break
