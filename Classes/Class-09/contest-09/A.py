
def solve2():
    dp = [None for i in range(101)]
    dp[1] = 1
    dp[2] = 1
    dp[3] = 0
    dp[4] = 1
    visited = [1,2,3,4]
    def solve(n,u):
        if n in visited:
            if dp[n]==1:
                return u
            else:
                return 1-u

        band =False
        if n%3 ==0:
            if solve(n-1,1-u)==u or solve(n-2,1-u)==u:
                band = True
        elif n%3 ==1:
            if solve(n-1,1-u)==u or solve(n-3,1-u)==u:
                band = True
        else:
            if solve(n-1,1-u)==u or solve(n-2,1-u)==u or solve(n-3,1-u)==u:
                band = True
        visited.append(n)
        if band:
            dp[n]=1
            return u
        else:
            dp[n]=0
            return 1-u

    n = int(input())

    ans = solve(n,0)

    print(ans+1)

solve2()

