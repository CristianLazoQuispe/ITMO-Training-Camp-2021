import math


def f(x):
    return x**2+math.sqrt(x)

c = float(input())

l = 0
r = math.sqrt(c)
esp = 10e-7
for i in range(25):
    m = l+(r-l)/2

    if abs(f(m)-c)<=esp:
        break
    if f(m)>c:
        r = m
    else:
        l = m

print(m)
