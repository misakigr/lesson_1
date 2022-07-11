n = 100
sum, sumkv, razn = 0, 0, 0
for i in range(n+1):
    sum += i
    sumkv += i**2
print(sum**2, sumkv)
print(sum**2 - sumkv)