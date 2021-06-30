# Function that returns the longest increasing subsequence
def answer(arr):
    n = len(arr)
    fenwick_tree = [0]*(n+1)
    sorted_arr = sorted(arr)
    dictionary = {}
    for i in range(n):
        dictionary[sorted_arr[i]] = i+1
    for i in range(n):
        arr[i] = dictionary[arr[i]]
    for i in range(n):
        index = arr[i]
        x = query(fenwick_tree, index-1)
        val = x+1
        while(index<=n):

            # Filling length at respective indexes
            fenwick_tree[index] = max(val, fenwick_tree[index])

            # Getting index of next node in fenwick tree
            index += index & (-index)

    ##************************************************##

    # Returning answer as query
    return query(fenwick_tree, n)
    
######### FUNCTION THAT CHECKS FOR MAX LENGTH TILL i'th INDEX ########
def query(f_tree, index):
    ans = 0

    # Traversing in fenwick tree from child to parent
    while index>0:
        ans = max(f_tree[index],ans)

        # Getting index of previous node in fenwick tree
        index -= index & (-index)
    return ans

###########################################

# Tesing our code
n = int(input())
ans = []
for i in range(n):
    ans.append(int(input()))
ans = ans[::-1]

ans = answer(ans)
print(ans)
ans = sorted(ans)
print(len(ans))
print(' '.join(list(map(str,ans))))
