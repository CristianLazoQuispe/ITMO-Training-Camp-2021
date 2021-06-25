

def solve(n):
    dp = [0]*(n+1)
    prev = [0]*(n+1)
    
    for i in range(1,n+1):

        if i%2 ==0 and i%3 == 0 :
            dp[i] = min(dp[i//2]+1,dp[i//3]+1,dp[i-1]+1)
            if dp[i] == dp[i//2]+1:
                prev[i] = i//2
            elif dp[i] == dp[i//3]+1:
                prev[i] = i//3
            else:
                prev[i]=i-1
        elif i%2 ==0 :
            dp[i] = min(dp[i//2]+1,dp[i-1]+1)
            if dp[i] == dp[i//2]+1:
                prev[i] = i//2
            else:
                prev[i]=i-1
        elif i%3 == 0 :
            dp[i] = min(dp[i//3]+1,dp[i-1]+1)
            if dp[i] == dp[i//3]+1:
                prev[i] = i//3
            else:
                prev[i]=i-1
        else:
            dp[i] = dp[i-1]+1
            prev[i]=i-1

    ans = []
    idx  = n
    while(idx > 0):
        ans.append(idx)
        idx = prev[idx]
    return ans[::-1]
n = int(input())

ans = solve(n)

ans = list(map(str,ans))
print(len(ans)-1)
print(' '.join(ans))
