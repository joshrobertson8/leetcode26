"""
LeetCode: 2024 10 23 09.12.56 Accepted Runtime 3ms Memory 12.3mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution:
    def twoSum(self,nums,target):
        hashmap = {}

        for i in range(len(nums)):
            hashmap[nums[i]] = i 

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return[i, hashmap[complement]]
        return []