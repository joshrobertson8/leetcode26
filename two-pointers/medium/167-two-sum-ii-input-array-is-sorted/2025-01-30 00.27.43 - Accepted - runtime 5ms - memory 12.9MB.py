"""
LeetCode: 2025 01 30 00.27.43 Accepted Runtime 5ms Memory 12.9mb

Algorithm:
Two pointers: start with l=0, r=len-1. While l < r, if sum equals target, return [l+1, r+1] (1-indexed). If sum > target, decrement r (reduce sum). If sum < target, increment l (increase sum). This leverages sorted property to find pair in O(n) time without extra space.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        l = 0 
        r = len(numbers) - 1

        while l < r:

            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1
        return [l + 1, r + 1]