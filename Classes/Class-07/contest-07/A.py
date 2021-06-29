def inputli():
    return list(map(int,input().split()))
def inputls():
    return input().split()
def inputlf():
    return list(map(float,input().split()))
 

[n,x,y,a0] = inputli()
[m,z,t,b0] = inputli()

#a = [0 for i in range(n)]
b = [0 for i in range(2*m)]
c = [0 for i in range(2*m)]
sum = [0 for i in range(n+1)]


a_back = a0
sum[0] = a_back
for i in range(1,n):
    a = (x*a_back+y)%(1<<16)
    sum[i] = sum[i-1]+a
    a_back = a

#print('a',a)

b[0] = b0
c[0] = b[0]%(n)
for i in range(1,2*m):
    b[i] = (z*b[i-1]+t)%(1<<30)
    #b[i] = powmod((z*b[i-1]+t),(1<<30))
    c[i] = b[i]%(n)

#print(a)
#print(b)
#print(c)
suma= 0
for i in range(m):
    l,r = min(c[2*i],c[2*i+1]),max(c[2*i],c[2*i+1])
    if l==0:
        aux = sum[r]
    else:
        aux = sum[r]-sum[l-1]
    suma += aux
print(suma)
#print(sum(ans))


