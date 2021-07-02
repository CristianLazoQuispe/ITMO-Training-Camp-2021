[n,m] = list(map(int,input().split()))

ai = list(map(int,input().split()))

aux = [[]for i in range(m)]
dp = [aux for i in range(n)]



#def grundy():

for i in range(n):
    for j in range(m):
        