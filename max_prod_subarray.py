"""max_product_subarray
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

[-2, 0, -1, -3, -6] -> 18
[5, 1, -5, -6, 3, 7] -> 450
"""


def maxProdSubarray(nums):
    max_prod = nums[0]
    min_prod = nums[0]
    glob_max_prod = nums[0]
    for i in nums[1:]:
        cur_max_prod = max(i, max_prod * i, min_prod * i)
        cur_min_prod = min(i, max_prod * i, min_prod * i)
        min_prod = cur_min_prod
        max_prod = cur_max_prod
        glob_max_prod = max(min_prod, max_prod, glob_max_prod)
    return glob_max_prod


if __name__ == "__main__":
    print(maxProdSubarray([2, 3, -2, 4]) == 6)
    print(maxProdSubarray([-2, 0, -1]) == 0)
    print(maxProdSubarray([-2, 0, -1, -3, -6]) == 18)
    print(maxProdSubarray([5, 1, -5, -6, 3, 7]) == 3150)
    print(maxProdSubarray([2, -1, 1, 1]) == 2)
