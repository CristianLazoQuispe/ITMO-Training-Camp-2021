def inputli():
    return list(map(int,input().split()))
def inputls():
    return input().split()
def inputlf():
    return list(map(float,input().split()))
 
 
def solve(elements):
    dp = [1]*len(elements)
    prev = [None]*len(elements)
 
    for i in range(len(elements)):
        dp[i]=1
        #j = bisect.bisect_right(elements,elements[i], lo=0, hi=i+1)-1

        for j in range(i):
            if elements[j]<=elements[i] and (dp[i]<(dp[j]+1)):
                #print(elements[j],elements[i])
                dp[i] = dp[j]+1
                prev[i] = j
    maxi = 0
    maxi_id = 0
    for i in range(len(elements)):
        if maxi<dp[i]:
            maxi = dp[i]
            maxi_id = i
 
    ans = []
    id = maxi_id
    while(id is not None):
        value = elements[id]
        ans.append(len(elements)-id)
        id = prev[id]
    return ans[::-1]
 
n = int(input())
ans = []
for i in range(n):
    ans.append(int(input()))
ans = ans[::-1]
ans = solve(ans)
ans = sorted(ans)
print(len(ans))
print(' '.join(list(map(str,ans))))
