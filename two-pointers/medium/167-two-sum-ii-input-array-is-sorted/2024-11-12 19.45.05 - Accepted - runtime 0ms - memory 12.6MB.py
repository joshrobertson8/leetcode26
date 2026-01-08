"""
LeetCode: 2024 11 12 19.45.05 Accepted Runtime 0ms Memory 12.6mb

Algorithm:
Hash map approach: store each number and its index+1 in hashmap. For each number, check if complement (target - number) exists in hashmap. If found, return indices. This works but doesn't leverage sorted property of array.

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