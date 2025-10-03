from collections import Counter


def solve(nums: list) -> int:
    cnt = Counter(nums)
    unique = sorted(cnt.keys())
    first = second = 0
    prev = 0
    for el in unique:
        if prev != 0 and el == prev + 1:
            first, second = second, max(second, first + el * cnt[el])
        else:
            first, second = second, second + el * cnt[el]
        prev = el
    return second

print(solve([3,4,2]))
print(solve([2,2,3,3,3,4]))
