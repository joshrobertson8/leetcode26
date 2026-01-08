"""
LeetCode: 2024 11 11 09.16.04 Accepted Runtime 90ms Memory 20.1mb

Algorithm:
TODO: Describe your approach here

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