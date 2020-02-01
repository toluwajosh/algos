"""There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

"""


"""Testcases

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
[100, 101, 102]
"""


def combine_arrays(L, R):
    arr = L + R
    i = j = k = 0
    # compare data from L and R and replace in arr
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    # Checking if any element was left
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
    return arr


def findMedianSortedArrays(nums1, nums2):
    nums_all = combine_arrays(nums1, nums2)
    print(nums_all)

    # find median
    nums_len = len(nums_all)
    if nums_len % 2 == 1:
        median = nums_all[nums_len // 2]
    else:
        median = (nums_all[nums_len // 2 - 1] + nums_all[nums_len // 2]) / 2
    return median


if __name__ == "__main__":
    nums1 = [1, 2, 5, 8, 9]
    nums2 = [3, 4, 45, 69, 82]
    print(combine_arrays(nums1, nums2))

    # print(findMedianSortedArrays(nums1, nums2))
