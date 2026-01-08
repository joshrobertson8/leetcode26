"""
LeetCode: 2024 10 23 09.12.56 Accepted Runtime 3ms Memory 12.3mb

Algorithm:
Two-pass hash map: first pass stores each number and its index in hashmap. Second pass, for each number, check if complement exists in hashmap and its index differs from current index. Return the two indices. O(n) time with two passes.

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