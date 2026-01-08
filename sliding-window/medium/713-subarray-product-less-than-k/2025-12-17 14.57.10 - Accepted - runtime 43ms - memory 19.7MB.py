"""
LeetCode: 2025 12 17 14.57.10 Accepted Runtime 43ms Memory 19.7MB

Algorithm:
Sliding window: expand window by multiplying product with nums[r]. While product >= k, shrink window from left (divide by nums[l], increment l). For each valid window [l, r], all subarrays ending at r with start >= l are valid. Count them as (r - l + 1). This counts all subarrays with product < k.

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

            while product >= k and r >= l:
                product = product // nums[l]
                l += 1
            count += (r - l + 1)
        return count
