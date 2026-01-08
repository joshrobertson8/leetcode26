"""
LeetCode: 2025 10 06 23.14.17 Accepted Runtime 91ms Memory 32.8MB

Algorithm:
Kadane's algorithm: maintain curSum (current subarray sum) and maxSum. For each number, if curSum is negative, reset it to 0 (starting fresh is better). Add current number to curSum and update maxSum. This finds the maximum sum contiguous subarray in one pass.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # max subarray screams kadanes algorithm


        curSum = 0
        maxSum = nums[0]

        for n in nums: 

            curSum = max(curSum, 0)

            curSum += n

            maxSum = max(maxSum, curSum)

        return maxSum