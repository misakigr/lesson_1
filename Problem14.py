# Самая длинная последовательность Коллатца
n = 1000000
m = 0
k = 0
razl = []
razlmax = []
for i in range(n):
    if m < k:
        m = k
        razlmax = razl
    razl = [i]
    k = 1
    while i > 1:
        k += 1
        if i % 2 == 0:
            i = i / 2
            razl.append(int(i))
        else:
            i = i * 3 + 1
            razl.append(int(i))
print(m, razlmax)
