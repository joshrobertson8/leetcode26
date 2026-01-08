"""
LeetCode: 2025 12 21 16.54.29 Accepted Runtime 19ms Memory 18.3MB

Algorithm:
Work backwards: start from the last index (end). For each position i, if nums[i] >= end - i (can reach end from i), update end to i. If we can reach end from position i, then i becomes the new target. Finally check if end == 0 (can reach last index from start).

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        

        n = len(nums)
        end = n - 1
        
        for i in range(n - 1, -1, -1):

            if nums[i] >= end - i:
                end = i

        
        return end == 0