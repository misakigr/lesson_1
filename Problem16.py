# 2**15 = 32768, сумма цифр этого числа равна 3 + 2 + 7 + 6 + 8 = 26.
#
# Какова сумма цифр числа 2**1000?
s = 1000
st = 2 ** s
summa =  0
for i in range(int(len(str(st)))+1):
    if i>0:
        print((int(str(st)[(i-1):i])))
        summa += int(str(st)[(i-1):i])

print(st, len(str(st)), summa)