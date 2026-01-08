"""
LeetCode: 2026 01 02 15.46.24 Accepted Runtime 0ms Memory 17.5MB

Algorithm:
Dynamic programming: dp[i] represents maximum money robbed up to house i. Base cases: dp[0] = nums[0], dp[1] = max(nums[0], nums[1]). For each house i >= 2, dp[i] = max(dp[i-2] + nums[i], dp[i-1]) (rob current house + best from i-2, or skip current and take best from i-1). Return dp[n-1].

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n

        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        
        return dp[n - 1]