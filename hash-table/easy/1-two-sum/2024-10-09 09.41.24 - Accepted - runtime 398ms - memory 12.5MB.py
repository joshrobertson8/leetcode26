"""
LeetCode: 2024 10 09 09.41.24 Accepted Runtime 398ms Memory 12.5mb

Algorithm:
Two-pass approach: first pass stores each number and its index in hashmap. Second pass, for each number, check if complement exists in nums array and hashmap index differs from current index. This uses both hashmap and array lookup, less efficient than pure hashmap approach.

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