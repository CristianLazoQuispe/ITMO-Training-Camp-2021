class Node:
    def __init__(self, v, label):
        self.node = v
        self.edgeLabel = label
         
N = int(input())

adj = [[] for i in range(N)]
 
freq = [0 for i in range(N)]
 
def dfs(u = 0, p = 0):     
    global N
     
    # Add the current node to
    # size of subtree rooted at u
    sz = 1
     
    # Iterate over its childern
    for a in adj[u]:
         
        # Check if child is not parent
        if a.node != p:
             
            # Get the subtree size
            # for the child
            val = dfs(a.node, u)
             
            # Set the frequency
            # of the current edge
            freq[a.edgeLabel] = val * (N - val)
            print(a.edgeLabel,'freq',freq[a.edgeLabel],N,val,val*(N-val))
             
            # Add the subtree size
            # to itself
            sz += val
             
    # Return the subtree size
    return sz
 
# Function to add edge between nodes
def addEdge(u, v, label):
     
    adj[u].append(Node(v, label))
    adj[v].append(Node(u, label))
     
# Function to print the frequencies
# of each edge in all possible paths
def printFrequencies():
     
    # Stores the frequency
    # of all the edges
    global N
     
    # Perform DFS
    dfs()
     
    for i in range(1, N):
        print(freq[i], end = " ")

label = 1
for i in range(N-1):
    [a,b] = list(map(int,input().split()))
    addEdge(a-1,b-1,label)
    label+=1
 
printFrequencies()
     
# This code is contributed by Stuti Pathak
