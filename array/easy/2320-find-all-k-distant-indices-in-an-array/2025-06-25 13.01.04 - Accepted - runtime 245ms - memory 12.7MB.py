"""
LeetCode: 2025 06 25 13.01.04 Accepted Runtime 245ms Memory 12.7mb

Algorithm:
For each index i, check all indices j to see if nums[j] equals key and the distance |i-j| is at most k. If such a j is found, add i to the result and break (to avoid duplicates). This finds all indices that are within k distance of at least one occurrence of key.

Time Complexity: O(n^2)
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