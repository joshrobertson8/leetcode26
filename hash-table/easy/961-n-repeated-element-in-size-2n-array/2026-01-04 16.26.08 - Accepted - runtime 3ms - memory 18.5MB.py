"""
LeetCode: 2026 01 04 16.26.08 Accepted Runtime 3ms Memory 18.5MB

Algorithm:
Use Counter to count frequencies of all numbers. Since array has 2n elements and one number appears n times, that number will have frequency n. Iterate through counter items and return the number with frequency equal to n // 2.

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