"""
LeetCode: 2026 01 05 17.12.46 Accepted Runtime 311ms Memory 36.9MB

Algorithm:
Make two passes: forward then backward.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        n = len(nums)

        prefixSum = [0] * n
        total = 0
        for i in range(n):
            total += nums[i]
            prefixSum[i] = total

        suffixMin = [0] * n
        suffixMin[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffixMin[i] = min(nums[i], suffixMin[i + 1])

        res = -math.inf
        for i in range(n - 1):
            res = max(res, (prefixSum[i] - suffixMin[i + 1]))

        return res