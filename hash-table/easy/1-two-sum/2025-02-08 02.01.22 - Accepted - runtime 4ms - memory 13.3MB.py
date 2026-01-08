"""
LeetCode: 2025 02 08 02.01.22 Accepted Runtime 4ms Memory 13.3mb

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