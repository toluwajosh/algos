"""largest rectangle in histogram


Example
[1,3,2,1,2] -> 5
"""


def largestRectangleInHistogram(nums):
    starts_dict = {}
    prev_num = 0
    max_area = cur_area = 0
    for i, num in enumerate(nums):
        if num > prev_num:
            cur_area = num
            starts_dict[num] = i
        elif num < prev_num:
            # calculate an area
            cur_area = (i - starts_dict[nums[i - 1]]) * nums[i - 1]
            # inherit start point
            cur_start = starts_dict[nums[i - 1]]
            del starts_dict[nums[i - 1]]
            if num not in starts_dict:
                starts_dict[num] = cur_start
        else:
            cur_area = (i - starts_dict[nums[i - 1]] + 1) * nums[i - 1]

        max_area = max(max_area, cur_area)
        prev_num = num
    return max_area


def largestRectangleInHistogramWithStack(nums):
    lengths = starts = []
    prev_num = 0
    max_area = cur_area = 0
    for i, num in enumerate(nums):
        if num > prev_num:
            cur_area = num
            starts_dict[num] = i
        elif num < prev_num:
            # calculate an area
            cur_area = (i - starts_dict[nums[i - 1]]) * nums[i - 1]
            # inherit start point
            cur_start = starts_dict[nums[i - 1]]
            del starts_dict[nums[i - 1]]
            if num not in starts_dict:
                starts_dict[num] = cur_start
        else:
            cur_area = (i - starts_dict[nums[i - 1]] + 1) * nums[i - 1]

        max_area = max(max_area, cur_area)
        prev_num = num
    return max_area


if __name__ == "__main__":
    print(largestRectangleInHistogram([1, 0, 2, 2, 10, 10]))
    print(largestRectangleInHistogram([1, 3, 0, 0, 4, 4]))
    print(largestRectangleInHistogram([1, 1, 1, 1, 1, 1, 2]))
    print(largestRectangleInHistogram([1, 2, 3, 4, 5, 3, 3, 2]))
    
    # with stack
    print(largestRectangleInHistogramWithStack([1, 0, 2, 2, 10, 10]))
    print(largestRectangleInHistogramWithStack([1, 3, 0, 0, 4, 4]))
    print(largestRectangleInHistogramWithStack([1, 1, 1, 1, 1, 1, 2]))
    print(largestRectangleInHistogramWithStack([1, 2, 3, 4, 5, 3, 3, 2]))
