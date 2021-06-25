def inputli():
    return list(map(int,input().split()))
def inputls():
    return input().split()
def inputlf():
    return list(map(float,input().split()))

def lcs(a,b):

    dp = [[0]*(len(b)+1) for i in range(len(a)+1)]
    maxi = 0
    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            maxi = max(maxi,dp[i][j])
    return maxi

def dist(a,b):
    dp = [[0]*(len(b)+1) for i in range(len(a)+1)]

    for i in range(1, len(a) + 1):
        dp[i][0] = i                    
    for j in range(1, len(b) + 1):
        dp[0][j] = j    

    mini = 0
    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):
            if a[i-1] == b[j-1]:
                cost = 0#dp[i][j] = dp[i-1][j-1]+1
            else:
                cost = 1
            
            dp[i][j] = min(dp[i-1][j]+1,
                            dp[i][j-1]+1,dp[i-1][j-1]+cost)
            mini = min(mini,dp[i][j])
    return dp[len(a)][len(b)]
    

a = input()
b = input()

#cnt = lcs(a,b)
#print(cnt,len(a)-cnt)
#print(len(a)-cnt)
ans = dist(a,b)
print(ans)
