"""
LeetCode: 2024 11 11 09.16.04 Accepted Runtime 90ms Memory 20.1mb

Algorithm:
Two pointers from both ends: start with left=0, right=len-1. Calculate area = width * min(height[left], height[right]). Update max_area. Move pointer with smaller or equal height (left++ if height[left] <= height[right], else right--). Continue until pointers meet. This maximizes area by always moving the shorter line.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left
            max_area = max(max_area, min(height[left], height[right]) * width)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_area