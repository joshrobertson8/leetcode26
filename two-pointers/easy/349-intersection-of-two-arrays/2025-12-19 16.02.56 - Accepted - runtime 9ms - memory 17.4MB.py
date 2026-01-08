"""
LeetCode: 2025 12 19 16.02.56 Accepted Runtime 9ms Memory 17.4MB

Algorithm:
Iterate through nums1.

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