import math 
def solve(arr: list) -> int:
    n = len(arr)
    matrix = [[math.inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i > j-2: matrix[i][j] = 0
    for l in range(2, n): # solve problem from single triangles. The index is 2 since array starts from 0
        for i in range(n-l): # how many triangles can you consider? n-2 
            j = i+l
            for k in range(i-1, j):
                matrix[i][j] = min(matrix[i][j], arr[i]*arr[k]*arr[j]+matrix[i][k] + matrix[k][j])

    return int(matrix[0][n-1])

print(solve([1,2,3]))
print(solve([1,3,1,4,1]))
