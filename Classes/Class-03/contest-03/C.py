def inputli():
    return list(map(int,input().split()))
def inputls():
    return input().split()
def inputlf():
    return list(map(float,input().split()))



def solve(n,M,weights,values):
    # maxi weight < M
    # target : maximum value
    
    dp = [[0]*(M+1) for i in range(n+1)]

    prev = [0]*n
    for i in range(1,n+1):
        for w in range(1,M+1):
            if weights[i-1]<=w:                
                dp[i][w] = max(values[i-1]+dp[i-1][w-weights[i-1]],dp[i-1][w]) 
            else:
                dp[i][w] = dp[i-1][w]
                
    maxi_values = dp[n][M]

    #print(maxi_values)
    #print(dp)
    w = M
    ans = []
    for i in range(n+1, 0, -1):
        if maxi_values <= 0:
            break
        if maxi_values == dp[i - 1][w]:
            continue
        else: 
            ans.append(i)
            maxi_values = maxi_values - values[i - 1]
            w = w - weights[i - 1]
            #print(w,weights[i - 1],i)
    return ans[::-1]
[n,M] = inputli()

weights = inputli()
values  = inputli()

ans= solve(n,M,weights,values)
print(len(ans))

ans = map(str,ans)
print(' '.join(ans))
