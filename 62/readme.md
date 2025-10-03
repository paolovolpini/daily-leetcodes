## Problem
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

Example 2:

Input: m = 3, n = 2\
Output: 3\
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

## Approach
The problem is actually pretty simple. You can get to the tile `grid[i][j]` either from `grid[i-1][j]` or `grid[i][j-1]`, thus the number of paths from `grid[0][0]` to `grid[i][j]` is the sum of the number of paths to `grid[i-1][j]` and the number of paths to `grid[i][j-1]`

