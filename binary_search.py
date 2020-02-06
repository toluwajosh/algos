"""binary_search
"""


def binary_search(array, number):
    left = 0
    right = len(array)
    while left < right:
        mid = left + (right - left) // 2
        print(mid)
        if array[mid] > number:
            right = mid
        else:
            left = mid + 1
    return left - 1


if __name__ == "__main__":
    print(binary_search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 10))
