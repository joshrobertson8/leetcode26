"""
LeetCode: 2024 10 02 17.22.42 Accepted Runtime 26ms Memory 11.7mb

Algorithm:
Sort the array first. Iterate through sorted array, storing indices where value equals target in a dictionary (result). Return sorted list of keys (indices). This finds all positions where target appears in sorted array.

Time Complexity: O(n log n)
Space Complexity: O(n)
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