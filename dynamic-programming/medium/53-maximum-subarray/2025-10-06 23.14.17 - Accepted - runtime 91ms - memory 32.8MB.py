"""
LeetCode: 2025 10 06 23.14.17 Accepted Runtime 91ms Memory 32.8MB

Algorithm:
Iterate through nums.

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