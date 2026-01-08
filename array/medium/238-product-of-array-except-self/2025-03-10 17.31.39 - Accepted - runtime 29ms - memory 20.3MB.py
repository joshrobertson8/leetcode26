"""
LeetCode: 2025 03 10 17.31.39 Accepted Runtime 29ms Memory 20.3mb

Algorithm:
Two-pass approach: first pass calculates prefix products, second pass multiplies by suffix products.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)
        answer = [1] * n 

        pre = 1
        for i in range(n):
            answer[i] = pre
            pre *= nums[i]

        post = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= post
            post *= nums[i]
        
        return answer