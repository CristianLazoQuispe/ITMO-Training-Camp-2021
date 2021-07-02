n = int(input())
graph = [[] for i in range(n)]
weight = [[] for i in range(n)]
root = -1
for i in range(n):
    [a,b] = list(map(int,input().split()))
    weight[i] = b
    if a == 0:
        root = i
    else:
        a-=1
        graph[a].append(i)

dp = [[None,None] for i in range(n)]

def dfs(v):
    dp[v][0] = 0
    dp[v][1] = weight[v]
    for u in graph[v]:
        dfs(u)
        dp[v][0] += max(dp[u][0],dp[u][1])
        dp[v][1] += dp[u][0]
dfs(root)

print(max(dp[root][0],dp[root][1]))
