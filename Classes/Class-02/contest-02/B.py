def solve(arr):
    if len(arr) <= 1:
        return 0, arr
    half = len(arr) // 2
    left_ans, left = solve(arr[:half])
    right_ans, right = solve(arr[half:])
    cross_ans = 0
    j = 0
    for i in range(len(left)):
        while j < len(right) and left[i] > right[j]:
            j += 1
        cross_ans += j
    return left_ans + cross_ans + right_ans, sorted(left + right)

n = int(input())
elements = list(map(int,input().split()))

print(solve(elements)[0])
