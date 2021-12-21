import math as m
for i in range(100,1000):
    sum = 0
    t = i
    while t > 0:
        r = t%10
        f = m.factorial(r)
        sum += f
        t //= 10
    if sum == i:
        print(i,end=' ')

