
[t,p] = map(int,input().split())

if p>20:
    speed = 1.0*t/(100-p)
    ans = speed*(p-20)+2*speed*20
    print(ans)
else:
    speed = 1.0*t/(2*(20-p)+80)
    ans = 2*speed*p
    print(ans)
