


n = int(input())

aux = [[] for i in range(n)] 
graph = [aux.copy() for i in range(n)]

for i in range(n):
    aux = list(map(int,input().split()))
    for j in range(n):
        graph[i][j] = aux[j]

aux = [1000000000000000 for i in range(n)] 
dp = [aux.copy() for i in range(1<<n)]

aux = [[None,None] for i in range(n)] 
from_ = [aux.copy() for i in range(1<<n)]

for i in range(n):
    dp[1<<i][i] = 0
    from_[1<<i][i] = [-1,-1]


for mask in range(1,1<<n):
    for v in range(n):
        if mask & (1<<v):
            for u in range(n):
                if not(mask &(1<<u)):
                    nmask = mask | (1<<u)
                    #print(dp[nmask][u])
                    if (dp[nmask][u] > dp[mask][v] + graph[v][u]):
                        dp[nmask][u] = dp[mask][v] + graph[v][u]
                        from_[nmask][u] = [mask, v]

ans = 100000000000000987
v = -1

for i in range(n):
    if ans>dp[(1<<n)-1][i]:
        ans = dp[(1<<n)-1][i]
        v = i
print(ans)

path = []
mask = (1<<n)-1

while(v!= -1):
    path.append(v+1)
    [mask,v] = from_[mask][v]
    #print(mask,v)

path = path[::-1]

print(' '.join(list(map(str,path))))
