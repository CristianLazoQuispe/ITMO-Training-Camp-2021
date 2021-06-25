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
 
revisted = [False for i in range(n)]
visited = [False for i in range(n)]
colors = [-1 for i in range(n)]
 
for i in range(m):
    [u,v] = inputli()
    adj_list[u-1].append(v-1)
    #print(adj_list)
 
order = []
 
def dfs(u):
    band = True
    visited[u]= True
    revisted[u] = True
    for v in adj_list[u]:
        #print(u+1,v+1)
        if visited[v] is False:
            if dfs(v) == False:
                return False
        elif revisted[v] == True:
            return False
    if band is False:
        return False
    order.append(u+1)
    revisted[u] = False
    return True


def solve():
    band = True

    for u in range(n):
        if not visited[u]:
            band = dfs(u) 
            if band is False:
                break

    if band is False:
        print(-1)
    else:
        print(*order[::-1]) 

t = threading.Thread(target=solve)
t.start()
t.join()

