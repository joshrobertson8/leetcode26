"""
LeetCode: 2024 10 23 09.12.56 Accepted Runtime 3ms Memory 12.3mb

Algorithm:
Use a hash map to track seen values. Use nested loops to check all pairs.

Time Complexity: O(n)
Space Complexity: O(n)
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