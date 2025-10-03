def solve(nums: list) -> int:
    first = second = 0
    for el in nums:
        first, second = second, max(second, first + el)
    return second

print(solve([1,2,3,1]))
print(solve([2,7,9,3,1]))
