"""
LeetCode: 2024 11 02 21.00.39 Accepted Runtime 1ms Memory 12.4mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
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