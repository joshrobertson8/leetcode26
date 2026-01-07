"""
LeetCode: 2025 02 23 22.04.44 Accepted Runtime 3ms Memory 12.6mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
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