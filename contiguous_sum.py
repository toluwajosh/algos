"""contiguous sum
Write a function that, 
given a list of integers (both positive and negative)
returns the sum of the contiguous subsequence with maximum sum.
Thus, given the sequence (1, 2, -4, 1, 3, -2, 3, -1) it should return 5.
"""

def contiguous_sum(array):
    max_current = max_global = array[0]
    for i in range(1, len(array)):
        max_current = max(array[i], max_current+array[i])
        max_global = max(max_current, max_global)
    return max_global

if __name__ == "__main__":
    print(contiguous_sum([1, 2, -4, 1, 3, -2, 3, -1]))
    print(contiguous_sum([-4, -1, 1, 2, 3, -1, 6]))