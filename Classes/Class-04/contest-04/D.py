import sys
import threading

sys.setrecursionlimit(10**6+1)
threading.stack_size(10**8)




    
def inputli():
    return list(map(int,input().split()))
def inputls():
    return input().split()
def inputlf():
    return list(map(float,input().split()))

 
[n,m] = inputli()
 
adj_list =[[] for i in range(n)]
visited = [False for i in range(n)]
colors = [-1 for i in range(n)]
 
for i in range(m):
    [u,v] = inputli()
    adj_list[u-1].append(v-1)
    adj_list[v-1].append(u-1)    
    #print(adj_list)
 
 
def dfs(u,group_id):
    visited[u]= True
    colors[u]=group_id
    for v in adj_list[u]:
        if colors[v] == -1:
            if dfs(v,1-group_id) is False:
                return False
        else:
            if colors[v] == group_id:
                return False
    return True


def solve():
    band = True
    for u in range(n):
        if not visited[u]:
            if dfs(u,0) is False:
                band = False
                break
    if band is False:
        print('NO')
    else:
        print('YES')
        for i in range(n):
            colors[i]+=1
        print(*colors) 
 
t = threading.Thread(target=solve)
t.start()
t.join()


