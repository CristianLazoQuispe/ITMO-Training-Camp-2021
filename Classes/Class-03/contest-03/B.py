def inputli():
    return list(map(int,input().split()))
def inputls():
    return input().split()
def inputlf():
    return list(map(float,input().split()))
 
def solve(n,m,matrix):

    dp = [[0]*(m) for i in range(n)]

    dp[0][0] = matrix[0][0]

    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + matrix[i][0]
    for j in range(1, m):
        dp[0][j] = dp[0][j-1] + matrix[0][j]
        
    for i in range(1,n):
        for j in range(1,m):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + matrix[i][j]
            #print(i,j,dp[i][j])
    #print(dp)
    #print(dp[n-1][m-1])
    return dp[n-1][m-1]


[n,m] = inputli()

matrix = []
for i in range(n):
    matrix.append(inputli())

#print(matrix)
ans = solve(n,m,matrix)
print(ans)
