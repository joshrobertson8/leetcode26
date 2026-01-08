"""
LeetCode: 2024 10 09 09.41.17 Accepted Runtime 386ms Memory 12.6mb

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
            if comp in nums and hashmap[comp] != i:
                return [i, hashmap[comp]]
        return []