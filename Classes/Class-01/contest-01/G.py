n = int(input())
statements = map(int,input().split())

cnt = {}

for i in statements:
    if i in cnt:
        cnt[i]+=1
    else:
        cnt[i]=1


maxi = 0
for i in cnt:
    if cnt[i] == i:
        maxi = max(maxi,cnt[i])

if maxi == 0 and 0 in cnt:
    print(-1)
else:
    print(maxi)
