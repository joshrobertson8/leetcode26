"""
LeetCode: 2025 06 25 13.01.04 Accepted Runtime 245ms Memory 12.7mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        
        result = []

        for i in range(len(nums)):
            for j in range(len(nums)):

                if nums[j] == key and abs(i - j) <= k:
                    result.append(i)
                    break
        return result