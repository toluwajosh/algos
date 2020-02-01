"""max area
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""

def maxArea(height):
    head = len(height) -1
    tail = 0
    max_area = min(height[head], height[tail]) * (head - tail)
    while head > tail:
        cur_area = min(height[head], height[tail]) * (head - tail)
        if height[head] < height[tail]:
            head -= 1
        else:
            tail += 1
        
        if cur_area > max_area:
            max_area = cur_area
    return max_area

if __name__ == "__main__":
    pass