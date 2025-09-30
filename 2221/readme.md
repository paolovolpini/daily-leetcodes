## Problem
You are given a 0-indexed integer array nums, where nums[i] is a digit between 0 and 9 (inclusive).

The triangular sum of nums is the value of the only element present in nums after the following process terminates:

1. Let nums comprise of n elements. If n == 1, end the process. Otherwise, create a new 0-indexed integer array newNums of length n - 1.
2. For each index i, where 0 <= i < n - 1, assign the value of newNums[i] as (nums[i] + nums[i+1]) % 10, where % denotes modulo operator.
3. Replace the array nums with newNums.
4. Repeat the entire process starting from step 1.

Return the triangular sum of nums.

## Approach
The approach is actually given in the text of the problem. What we can add is the fact that we do not need an additiona O(n) space, since we can use the array `nums` given as input. Each iteration we start from the second element and calculate the sum `nums[i-1] + nums[i]` and `nums[i+1] + nums[i]`. Then we assing the first sum to `nums[i-1]` and the second sum to `nums[i]`. Finally we return `nums[0]`.
