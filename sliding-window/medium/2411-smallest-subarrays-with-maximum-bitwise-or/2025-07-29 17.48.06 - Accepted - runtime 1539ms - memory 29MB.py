"""
LeetCode: 2025 07 29 17.48.06 Accepted Runtime 1539ms Memory 29MB

Algorithm:
Work backwards: for each position i, track last occurrence of each bit position (0-31) in last array. For each bit set in nums[i], update last[b] = i. Find maximum last occurrence across all bits (max_dist). The smallest subarray starting at i with maximum OR ends at max_dist, so length is max_dist - i + 1. This finds smallest subarray with maximum OR for each starting position.

Time Complexity: O(n^2)
Space Complexity: O(1)
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