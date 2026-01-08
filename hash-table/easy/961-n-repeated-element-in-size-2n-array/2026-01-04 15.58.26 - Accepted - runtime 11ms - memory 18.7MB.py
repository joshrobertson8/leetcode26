"""
LeetCode: 2026 01 04 15.58.26 Accepted Runtime 11ms Memory 18.7MB

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
