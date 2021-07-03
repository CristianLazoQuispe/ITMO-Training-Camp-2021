import sys
import threading

sys.setrecursionlimit(10**6+1)
threading.stack_size(10**8)

def solve():
    [n,m] = list(map(int,input().split()))

    matrix = [[] for i in range(n)]

    for i in range(n):
        aux = list(map(int,input().split()))
        matrix[i] = aux

    levels = [-1 for i in range(n)]
    visited = [False for i in range(n)]

    m = m-1
    queue = []
    queue.append(m)
    levels[m]=0

    def bfs(matrix):
        while(len(queue)>0):
            u = queue.pop(0)
            visited[u] =True
            new_level = levels[u]+1
            for i in range(n):
                #print(u,i)
                if matrix[u][i] == 1:
                    if not visited[i]:
                        levels[i] = new_level
                        visited[i] =True
                        queue.append(i)


    bfs(matrix)
    #print(visited)
    levels = list(map(str,levels))
    print(' '.join(levels))

t = threading.Thread(target=solve)
t.start()
t.join()





