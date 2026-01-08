"""
LeetCode: 2025 07 11 13.53.30 Accepted Runtime 4ms Memory 13.2mb

Algorithm:
To minimize the range, we want to maximize the minimum value (by adding k) and minimize the maximum value (by subtracting k). Calculate the new range as (max - k) - (min + k). If this is negative, return 0 (we can make all values equal).

Time Complexity: O(1)
Space Complexity: O(1)
"""

class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return max(0, (max(nums) - k) - (min(nums) + k))