"""
LeetCode: 2025 06 17 21.56.43 Accepted Runtime 0ms Memory 12.6mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        candidate = float('inf')
        answer = 0

        for num in nums:

            candidate = min(candidate, num)

            answer = max(answer, num - candidate)


        return -1 if answer == 0 else answer