## Problem
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]\
Output: 4\
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).\
Total amount you can rob = 1 + 3 = 4.

## Approach
The function that describes the problem is:

$$f(i) = \begin{cases}0 & \text{if } i \ge n\\ \max \{f(i+1), v[i] + f(i+2)\}\end{cases}$$

Supposing we have the solution for the subproblem $i-1$ and $i-2$, we can either then consider the solution for $i-1$ or the solution for $i-2$ plus the value v[i]. Thus we can solve this easily with Dynamic Programming.

A step forward consists in avoiding using an array, since we just need two values each time. Thus we can use $O(1)$ space.
