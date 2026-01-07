"""
LeetCode: 2024 10 07 17.56.17 Accepted Runtime 32ms Memory 12.3mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def searchInsert(self, nums, target):
        
        
        for i in range(len(nums)):

            if target == nums[i]:
                return i

            if target <= nums[i]:
                return i
        return i + 1