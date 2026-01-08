"""
LeetCode: 2024 10 09 09.41.36 Accepted Runtime 47ms Memory 12.4mb

Algorithm:
Two-pass hash map: first pass stores each number and its index in hashmap (value -> index). Second pass, for each number, check if complement (target - nums[i]) exists in hashmap and its index differs from current index. Return the two indices. O(n) time with two passes.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def twoSum(self,nums,target):
        hashmap = {}
        
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in hashmap and hashmap[comp] != i:
                return [i, hashmap[comp]]
        return []