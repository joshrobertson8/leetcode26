"""
LeetCode: 2026 01 04 16.26.08 Accepted Runtime 3ms Memory 18.5MB

Algorithm:
Use a Counter to count frequencies.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from collections import Counter

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        counts = Counter(nums)
        n = len(nums)
        
        for num, cnt in counts.items():
            if cnt == n // 2:
                return num