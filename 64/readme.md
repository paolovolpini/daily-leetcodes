## Problem
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:\
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]\
Output: 7\
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

## Approach
If we know the minimum paths to `grid[i-1][j]` and `grid[i][j-1]`, then we can simply take the minimum between these and sum the value to `grid[i][j]`. Thus the problem is easy.
