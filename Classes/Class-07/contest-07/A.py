def inputli():
    return list(map(int,input().split()))
def inputls():
    return input().split()
def inputlf():
    return list(map(float,input().split()))
 

[n,x,y,a0] = inputli()
[m,z,t,b0] = inputli()

#a = [0 for i in range(n)]
#b = [0 for i in range(2*m)]
#c = [0 for i in range(2*m)]
sum = [0 for i in range(n)]


a_back = a0
sum[0] = a_back

for i in range(1,n):
    a = (x*a_back+y)%(1<<16)
    sum[i] = sum[i-1]+a
    a_back = a

#print(sum)
#print(a)
#print(b)
#print(c)
suma= 0
b_2i_1 = b0

for i in range(m):
    if i == 0:
        b_2_i = b0
        c_2_i = (b_2_i)%n
    else:
        b_2_i = (z*b_2i_1+t)%(1<<30)
        c_2_i = (b_2_i)%n

    b_2i_1 = (z*b_2_i+t)%(1<<30)
    c_2i_1 = (b_2i_1)%n

    #print(b_2_i,b_2i_1)
    #print(c_2_i,c_2i_1)

    l,r = min(c_2_i,c_2i_1),max(c_2_i,c_2i_1)
    if l==0:
        aux = sum[r]
    else:
        aux = sum[r]-sum[l-1]
    suma += aux
print(suma)
#print(sum(ans))


