# k = 0
# summ = 0
#
# while k < 10:
#     razl = []
#     k += 1
#     for i in range(k):
#         summ += 1
#     for j in range(len(str(summ))+1):
#         if j > 0:
#             razl.append(summ / j)
#     print(summ, ":", razl)

n = 1
while n < 10:
    n += n
    razl = []
    k = 0
    for i in range(n + 1):
        if i > 0 and n % i == 0:
            razl.append(int(n / (n / i)))
            k += 1
    print(n, "(",k,"делител. )", ":", razl)
