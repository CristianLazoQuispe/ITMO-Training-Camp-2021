from collections import defaultdict


class my_Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = {}
    def addEdge(self,u,v,w):
        if u in self.graph:
            self.graph[u].append([v,w])
        else:
            self.graph[u] = [[v,w]]
    def topologicalSortUtil(self,v,visited,stack):
        visited[v] = True
        if v in self.graph.keys():
            for [node,weight] in self.graph[v]:
                if visited[node] == False:
                    self.topologicalSortUtil(node,visited,stack)
        stack.append(v)

    def shortestPath(self, s,to):
        #print(self.graph)
        visited = [False for i in range(self.V)]
        dist = [float("Inf") for i in range(self.V)]

        stack =[]
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(s,visited,stack)
        dist[s] = 0
        #print('stack',stack)
        while stack:
            i = stack.pop()
            #print(i,self.graph[i])
            if i in self.graph:
                for node,weight in self.graph[i]:
                    if dist[node] > dist[i] + weight:
                        dist[node] = dist[i] + weight
        
        mini = float("Inf")
        for i in range(self.V):
            if i == to:
                if dist[i] != float("Inf"):
                    mini = min(mini,dist[i])
        if mini == float("Inf"):
            print('Unreachable')
        else:
            print(mini)
'''

2 1 1 2
1 2 -10


2 1 2 1
1 2 -10


3 3 1 2
1 2 -10
1 2 -20
1 2 10
'''

[n,m,s,to] = list(map(int,input().split()))
s = s-1
to = to-1
g = my_Graph(n)

for i in range(m):
    [a,b,w] = list(map(int,input().split()))
    a = a-1
    b = b-1
    g.addEdge(a,b,w)
g.shortestPath(s,to)
