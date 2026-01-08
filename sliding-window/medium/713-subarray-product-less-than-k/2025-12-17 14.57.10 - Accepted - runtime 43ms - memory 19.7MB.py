"""
LeetCode: 2025 12 17 14.57.10 Accepted Runtime 43ms Memory 19.7MB

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
