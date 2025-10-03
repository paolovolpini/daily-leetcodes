def solve(m: int, n: int) -> int:
    if n == 1 or m == 1: return 1
    arr = [[1 for _ in range(n)] for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            arr[i][j] = arr[i-1][j] + arr[i][j-1]
    return arr[m-1][n-1]

print(solve(3, 7))
print(solve(3, 2))

