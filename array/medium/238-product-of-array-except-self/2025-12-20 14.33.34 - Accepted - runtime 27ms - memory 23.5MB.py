"""
LeetCode: 2025 12 20 14.33.34 Accepted Runtime 27ms Memory 23.5MB

Algorithm:
Two-pass approach: first pass calculates prefix products, second pass multiplies by suffix products.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        pre = 1
        for i in range(n): 
            res[i] *= pre
            pre *= nums[i]

        
        post = 1
        for i in range(n - 1, -1 , -1): 
            res[i] *= post
            post *= nums[i]

        return res