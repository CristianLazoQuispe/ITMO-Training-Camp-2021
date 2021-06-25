def inputli():
    return list(map(int,input().split()))
def inputls():
    return input().split()
def inputlf():
    return list(map(float,input().split()))
 
 
[n,m] = inputli()

adj_matrix = [[0]*n for i in range(n)]

for i in range(m):
    [u,v] = inputli()
    adj_matrix[u-1][v-1]=1
    adj_matrix[v-1][u-1]=1
    
for i in range(n):
    aux= [0]*n
    for j in range(n):
        aux[j] = str(adj_matrix[i][j])
    print(' '.join(aux))
