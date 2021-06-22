n = int(input())
first = map(int,input().split())
n = int(input())
second = map(int,input().split())


numbers = {}

for i in first:
    if i in numbers:
        numbers[i]+=1
    else:
        numbers[i]=1

for i in second:
    if i in numbers:
        print(numbers[i])
    else:
        print(0)
