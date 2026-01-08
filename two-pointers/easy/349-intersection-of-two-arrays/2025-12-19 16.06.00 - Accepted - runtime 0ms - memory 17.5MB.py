"""
LeetCode: 2025 12 19 16.06.00 Accepted Runtime 0ms Memory 17.5MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        s1 = set(nums1)
        s2 = set(nums2)

        return list(s1 & s2)