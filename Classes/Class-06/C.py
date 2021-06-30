import sys


def inputli():
    return list(map(int,input().split()))
def inputls():
    return input().split()
def inputlf():
    return list(map(float,input().split()))
 

N = 500003
 
tree = [0] * (2 * N)
 
def make_tree(arr) :
    for i in range(n) :
        tree[n + i] = arr[i]
    for i in range(n - 1, 0, -1) :
        tree[i] = tree[i << 1] + tree[i << 1 | 1]
        
def update(p, value) :
    tree[p + n] = value
    p = p + n
    i = p     
    while i > 1 :         
        tree[i >> 1] = tree[i] + tree[i ^ 1]
        i >>= 1
def query(l, r) : 
    res = 0
    l += n
    r += n
    while l < r :
        if (l & 1) :
            res += tree[l]
            l += 1
        if (r & 1) :
            r -= 1
            res += tree[r]             
        l >>= 1
        r >>= 1
    return res
 

import sys
import threading

sys.setrecursionlimit(10**6+1)
threading.stack_size(10**8)

n = int(input())

numbers = inputli()

make_tree(numbers)

def solve2():




    while(True):
        try:
            a = input().split()
            kind = a[0]
            i = int(a[1])
            j = int(a[2])

            if kind == '0':
                update(i-1,j)
            else:
                print(query(i-1,j))
        except EOFError :
            break
t = threading.Thread(target=solve2)
t.start()
t.join()


