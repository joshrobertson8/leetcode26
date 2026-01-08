"""
LeetCode: 2024 11 05 00.50.30 Accepted Runtime 0ms Memory 11.6mb

Algorithm:
Copy nums2 into the end of nums1 (starting at index m+i). Then sort the entire nums1 array. This merges both arrays by filling the extra space in nums1 with nums2, then sorting. Simple but O((m+n) log(m+n)) due to sorting.

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
            nums1[m+i] = nums2[i]

        nums1.sort()