"""
LeetCode: 2026 01 05 17.12.46 Accepted Runtime 311ms Memory 36.9MB

Algorithm:
First pass: build prefix sum array where prefixSum[i] is the sum of elements from 0 to i. Second pass: build suffix minimum array where suffixMin[i] is the minimum element from i to the end. For each split position i, calculate score as prefixSum[i] - suffixMin[i+1] (sum of left part minus minimum of right part). Return the maximum score.

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