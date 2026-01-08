"""
LeetCode: 2025 09 26 20.31.30 Accepted Runtime 117ms Memory 20.1mb

Algorithm:
Two pointers from both ends: start with l=0, r=n-1. Calculate area = width * min(height[l], height[r]). Update maxArea. Move pointer with smaller height (l++ if height[l] < height[r], else r--). Continue until pointers meet. This maximizes area by always moving the shorter line, as width decreases but height might increase.

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