"""
LeetCode: 2025 02 23 22.04.44 Accepted Runtime 3ms Memory 12.6mb

Algorithm:
An array is special if adjacent elements have different parity (one even, one odd). Check each adjacent pair: if both have the same parity (both even or both odd), return False. If all pairs have different parity, return True.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums) - 1):
            
            if nums[i] % 2 == nums[i + 1] % 2:
                return False
        return True