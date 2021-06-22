n = input()
elements = map(int,input().split())

elements = sorted(elements)
elements = map(str,elements)

print(' '.join(elements))
