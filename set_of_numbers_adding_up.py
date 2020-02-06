"""Set of numbers that add up to number

[2,4,6,10], 16
"""


def rec(nums, total, i):
    if total == 0:
        return 1
    elif total < 0:
        return 0
    elif i < 0:
        return 0
    elif total < nums[i]:
        return rec(nums, total, i - 1)
    else:
        return rec(nums, total - nums[i], i - 1) + rec(nums, total, i - 1)


def setOfNumbersAddingUp(nums, total):
    # first return all subsets [by dynamic programmming]
    return rec(nums, total, len(nums) - 1)


def dp(nums, total, i, mem):
    key = str(total) + ":" + str(i)
    if key in mem:
        return mem[key]
    if total == 0:
        return 1
    elif total < 0:
        return 0
    elif i < 0:
        return 0
    elif total < nums[i]:
        result = dp(nums, total, i - 1, mem)
    else:
        result = dp(nums, total - nums[i], i - 1, mem) + dp(nums, total, i - 1, mem)
    mem[key] = result
    return result


def setOfNumbersAddingUpDP(nums, total):
    mem = {}
    return dp(nums, total, len(nums) - 1, mem)


if __name__ == "__main__":
    print(setOfNumbersAddingUp([2, 4, 6, 10], 16))
    print(setOfNumbersAddingUpDP([2, 4, 6, 10], 16))
