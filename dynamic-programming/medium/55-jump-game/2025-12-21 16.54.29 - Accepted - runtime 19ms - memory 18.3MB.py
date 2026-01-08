"""
LeetCode: 2025 12 21 16.54.29 Accepted Runtime 19ms Memory 18.3MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        

        n = len(nums)
        end = n - 1
        
        for i in range(n - 1, -1, -1):

            if nums[i] >= end - i:
                end = i

        
        return end == 0