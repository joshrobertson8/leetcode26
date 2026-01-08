"""
LeetCode: 2025 06 13 14.20.26 Accepted Runtime 0ms Memory 12.3mb

Algorithm:
Sort the array first.

Time Complexity: O(n log n)
Space Complexity: O(1)
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        for i in range(n):
            nums1[m + i] = nums2[i]

        nums1.sort()