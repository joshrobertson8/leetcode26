"""
LeetCode: 2024 10 02 17.22.42 Accepted Runtime 26ms Memory 11.7mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def targetIndices(self, nums, target):
        
        if target not in nums:
            return []

        sorted_nums = sorted(nums)
        result = {}

        for i in range(len(sorted_nums)):
            if sorted_nums[i] == target:
                result[i] = sorted_nums[i]
        return sorted(result)