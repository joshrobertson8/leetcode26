"""
LeetCode: 2025 09 26 20.31.30 Accepted Runtime 117ms Memory 20.1mb

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
        n = len(height)
        l, r = 0, n - 1
        maxArea = 0

        for i in range(n):

            width = r - l

            maxArea = max(maxArea, width * min(height[r], height[l]))

            if height[l] < height[r]:

                l += 1
            
            else: 
                r -= 1

        return maxArea