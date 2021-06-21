reference = 'abc'

def solve(a, b,m,n):
 
    matrix = [[0] * (n + 1) for i in range(m + 1)]
 
    for i in range(m + 1):
        matrix[i][0] = 1
 
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + matrix[i - 1][j]                 
            else:
                matrix[i][j] = matrix[i - 1][j]
 
    return matrix[m][n]

sub = input()

print(solve(sub,reference,len(sub),len(reference)))
