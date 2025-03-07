"""Product except self

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).
"""


def productExceptSelf(nums):
    if len(nums) == 2:
        return [nums[1], nums[0]]
    result = productExceptSelf(nums[:2])


if __name__ == "__main__":
    pass
