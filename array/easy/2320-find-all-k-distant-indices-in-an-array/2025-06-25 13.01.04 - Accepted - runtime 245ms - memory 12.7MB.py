"""
LeetCode: 2025 06 25 13.01.04 Accepted Runtime 245ms Memory 12.7mb

Algorithm:
Nested loops to check all pairs.

Time Complexity: O(n²)
Space Complexity: O(n)
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