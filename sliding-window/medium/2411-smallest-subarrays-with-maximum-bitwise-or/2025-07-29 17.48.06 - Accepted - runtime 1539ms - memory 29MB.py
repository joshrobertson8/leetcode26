"""
LeetCode: 2025 07 29 17.48.06 Accepted Runtime 1539ms Memory 29MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(n²)
Space Complexity: O(n)
"""

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        last = [0] * 32
        res = [0] * n

        for i in range(n - 1, -1, -1):
            for b in range(32):
                if nums[i] & (1 << b):
                    last[b] = i

            max_dist = i
            for b in range(32):
                max_dist = max(max_dist, last[b])

            res[i] = max_dist - i + 1

        return res