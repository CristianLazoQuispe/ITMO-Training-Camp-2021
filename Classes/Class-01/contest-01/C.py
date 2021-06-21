def solve(a,b,m):

    if b==0:
        return 1
    else:
        if b%2==0:
            return (solve(a,b//2,m)**2)%m
        else:
            return ((a%m)*solve(a,b-1,m))%m
[a,b,m] = list(map(int, input().split(' ')))

print(solve(a,b,m))
    