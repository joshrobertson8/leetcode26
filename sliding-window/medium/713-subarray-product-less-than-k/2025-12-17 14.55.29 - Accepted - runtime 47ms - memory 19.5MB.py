"""
LeetCode: 2025 12 17 14.55.29 Accepted Runtime 47ms Memory 19.5MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
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
