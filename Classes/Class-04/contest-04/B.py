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
 
def print_matrix(adj_matrix,n):
    for i in range(n):
        aux= [0]*n
        for j in range(n):
            aux[j] = str(adj_matrix[i][j])
        print(' '.join(aux))
 
 
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
        if not visited[v]:
            #colors[v]=group_id
            dfs(v,group_id)
 



def solve():
    groupz =1

    for u in range(n):
        if not visited[u]:
            dfs(u,groupz)
            groupz+=1
    print(groupz-1)
    print(*colors) 
 
t = threading.Thread(target=solve)
t.start()
t.join()


