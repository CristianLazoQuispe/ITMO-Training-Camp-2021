def my_sorted(elements):


    count = [0 for i in range(101)]

    for i in elements:
        count[i]+=1
    for i in range(1,101):
        count[i]+=count[i-1]

    ans = [0 for i in elements]
    for i in elements:
        ans[count[i]-1] = i
        count[i]-=1

    return ans

elements = list(map(int,input().split()))

elements = my_sorted(elements)
elements = map(str,elements)

print(' '.join(elements))
