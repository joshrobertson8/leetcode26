"""
LeetCode: 2024 11 12 19.45.05 Accepted Runtime 0ms Memory 12.6mb

Algorithm:
Use a hash table to store seen elements for O(1) lookup.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        hashmap = {}
        
        for i in range(len(numbers)):
            complement = target - numbers[i]

            if complement in hashmap:
                return [hashmap[complement], i + 1]

            hashmap[numbers[i]] = i + 1