import sys
import threading

sys.setrecursionlimit(10**6+1)
threading.stack_size(10**8)

def solve():
    [n_v,m_e,s] = list(map(int,input().split()))

    graph = {}
    s = s-1
    for i in range(m_e):
        [u,v] = list(map(int,input().split()))
        if (u-1) in graph:
            graph[u-1].append(v-1)
        else:
            graph[u-1] = [v-1]


    dp = [0 for i in range(n_v)]
    visited = [False for i in range(n_v)]

    def dfs(graph,u):    
        dp[u] = 0
        visited[u]=True
        if u not in graph:
            return
        for v in graph[u]:
            if visited[v]:
                if dp[v] ==0:
                    dp[u]=1
                    break
            else:
                dfs(graph,v)
                if dp[v]==0:
                    dp[u]=1
                    break
        return 

    dfs(graph,s)
    #print(dp)
    #print(2-dp[s])
    if dp[s]==1:
        print('First player wins')
    else:
        print('Second player wins')


t = threading.Thread(target=solve)
t.start()
t.join()


