"""
LeetCode: 2025 07 11 13.53.30 Accepted Runtime 4ms Memory 13.2mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return max(0, (max(nums) - k) - (min(nums) + k))