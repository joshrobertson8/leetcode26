"""
LeetCode: 2024 11 02 21.00.39 Accepted Runtime 1ms Memory 12.4mb

Algorithm:
Two-pass hash map: first pass stores each number and its index in hashmap. Second pass, for each number, check if complement exists in hashmap and its index differs from current index. Return the two indices. O(n) time with two passes.

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
                return [i,hashmap[complement]]
        return 0