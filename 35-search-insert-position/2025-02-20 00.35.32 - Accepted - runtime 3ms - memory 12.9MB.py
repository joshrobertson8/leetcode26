"""
LeetCode: 2025 02 20 00.35.32 Accepted Runtime 3ms Memory 12.9mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def searchInsert(self, nums, target):

        for i in range(len(nums)):
            
            if nums[i] >= target:
                return i
        return len(nums)