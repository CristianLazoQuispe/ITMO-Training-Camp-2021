def f(n):
    if n<2:
        return n
    if n%2 ==0:
        return f(n//2)
    else:
        return f((n-1)//2)+f((n-1)//2+1)
ans = f(int(input()))
print(ans)
