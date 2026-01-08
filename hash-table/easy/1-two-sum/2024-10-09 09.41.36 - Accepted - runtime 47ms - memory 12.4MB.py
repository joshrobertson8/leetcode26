"""
LeetCode: 2024 10 09 09.41.36 Accepted Runtime 47ms Memory 12.4mb

Algorithm:
TODO: Describe your approach here

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