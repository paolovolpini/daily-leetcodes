def solve(nums: list) -> int:
    n = len(nums)
    l = n-1
    for _ in range(n-1):
        for j in range(1, l+1, 2):
            nums[j-1] = (nums[j-1] + nums[j]) % 10
            if j != l:
                nums[j] = (nums[j] + nums[j+1]) % 10
        l -= 1
    return nums[0]


print(solve([1,2,3,4,5]))
