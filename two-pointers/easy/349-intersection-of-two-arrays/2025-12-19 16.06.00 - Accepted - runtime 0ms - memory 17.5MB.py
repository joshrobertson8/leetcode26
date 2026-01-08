"""
LeetCode: 2025 12 19 16.06.00 Accepted Runtime 0ms Memory 17.5MB

Algorithm:
Direct implementation.

Time Complexity: O(1)
Space Complexity: O(n)
"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        s1 = set(nums1)
        s2 = set(nums2)

        return list(s1 & s2)