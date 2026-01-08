"""
LeetCode: 2025 01 31 15.52.21 Accepted Runtime 0ms Memory 13.2mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}

        for i in range(len(nums)):

            hashmap[nums[i]] = i 

        for i in range(len(nums)):

            complement = target - nums[i]

            if complement in hashmap and hashmap[complement] != i:
                return [hashmap[complement], i]

        return null