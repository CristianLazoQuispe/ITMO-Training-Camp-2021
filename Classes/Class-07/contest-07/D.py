def inputli():
    return list(map(int,input().split()))
def inputls():
    return input().split()
def inputlf():
    return list(map(float,input().split()))
 
import copy

logn = 0


def calc_depths(p):
    d = [-1 for i in range(len(p))]
    d[0] = 0
    for i in  range(1,len(p)):
        d[i] = d[p[i]]+1

    return d



def precalc(p):
    global logn
    n = len(p)
    logn =1
    while((1<<logn)<=n):
        logn+=1
    
    aux = [-1 for i in range(logn+1)]
    jmp = [aux.copy() for j in range(n)]

    for i in range(n):
        jmp[i][0] = p[i]
    
    jmp[0][0]=0

    for k in range(1,logn):
        for i in range(n):
            if (jmp[i][k-1]!=-1):
                jmp[i][k] = jmp[jmp[i][k-1]][k-1]

    return jmp

def findKth( a,  k,  dp):
    
    c = a    
    cur_level = k
    
    for i in range(logn,-1,-1): #(int i = LG; i >= 0; i--){
        #print(c,i)
        if (dp[c][i] != -1 and (1 << i) <= cur_level):
            c = dp[c][i]
            cur_level = cur_level - (1 << i)
    
    print("The ",k,"nd ancestor of ",a," is ",c,'\n')
    
n = int(input())

fathers = [[]for i in range(n+1)]
fathers[0] = -1

for idx,father in enumerate(inputli()):
    fathers[idx+1] = father
    #fathers[idx+1] -=1
print(fathers)

d = calc_depths(fathers)
print(d)
jmp = precalc(d)
print(jmp)

print(n,logn)
for i in range(n):
    for j in range(logn):
        findKth(i,1<<j,jmp)
