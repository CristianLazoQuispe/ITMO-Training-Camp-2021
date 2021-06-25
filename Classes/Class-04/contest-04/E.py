def inputli():
    return list(map(int,input().split()))
def inputls():
    return input().split()
def inputlf():
    return list(map(float,input().split()))
 
 
 class Edge:
    def __init__(self,from_,to,weight) -> None:
        self.from = from_
        self.to = to
        self.weight  = weight


graph = Edge()

visited = []
pathToT = []

def dfs(s,t):
    visited[s] = True
    if (s==t):
        pathToT[t] = 0
        return
    for e in graph[s]:
        if not visited[e.to]:
            df(e.to,s)
    for e in graph[s]:
        if pathToT[e.to] != -1:
            


[n,m] = input()
