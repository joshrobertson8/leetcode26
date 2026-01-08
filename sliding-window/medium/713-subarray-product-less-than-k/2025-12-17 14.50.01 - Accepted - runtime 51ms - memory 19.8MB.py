"""
LeetCode: 2025 12 17 14.50.01 Accepted Runtime 51ms Memory 19.8MB

Algorithm:
Use nested loops to check all pairs.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
        l = 0
        product = 1

        for r in range(len(nums)): 
            product *= nums[r]

            while product >= k and l <= r: 
                product = product // nums[l]
                l += 1
            count += (r - l + 1)
        return count
