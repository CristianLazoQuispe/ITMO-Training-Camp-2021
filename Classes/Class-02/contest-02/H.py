[n,x,y] = list(map(int,input().split()))


l = min(x,y)
r = n*max(x,y)

    
def copies(t):
    cntx = int((t-min(x,y))/x)
    cnty = int((t-min(x,y))/y)
    ans = 1+1+cntx+cnty
    #print(t,x,y,ans,cntx,cnty)
    return ans

while (l <= r):
    m = l+(r-l)//2
    if copies(m)<=n:
        l = m+1
    else:
        r = m-1

print(l)
