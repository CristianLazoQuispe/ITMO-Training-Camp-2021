def find_idx1(elements,x,l,r):

    while (l <= r):
        m = l+(r-l)//2
        if m<0 or m>len(elements)-1:
            break
        if elements[m]>=x:
            r = m-1
        else:
            l = m+1

    return l

def find_idx2(elements,x,l,r):
    while (l <= r):
        m = l+(r-l)//2
        if m<0 or m>len(elements)-1:
            break
        if elements[m]<=x:
            l = m+1
        else:
            r = m-1
    return r


def solve(elements,l,r):

    a = find_idx1(elements,l,0,len(elements)-1)
    b = find_idx2(elements,r,a,len(elements)-1)

    #print(l,'->' ,a,r,'->',b)

    #print(len(elements)-a-b+1)

    return max(b-a+1,0)

n = int(input())

elements = list(map(int,input().split()))

elements = sorted(elements)

m = int(input())


ans = []
for i in range(m):
    [l,r] = list(map(int,input().split()))

    ans.append(solve(elements,l,r))

ans = map(str,ans)

print(' '.join(ans))
