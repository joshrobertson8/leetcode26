"""
LeetCode: 2025 12 19 16.02.56 Accepted Runtime 9ms Memory 17.4MB

Algorithm:
Linear scan with set: iterate through nums1. For each num, if it's in nums2 and not already in result, append to result. This finds intersection by checking membership in nums2 and avoiding duplicates.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        res = []
        
        for num in nums1: 
            if num in nums2 and num not in res: 
                res.append(num)
        return res