"""
LeetCode: 2024 11 26 12.04.18 Accepted Runtime 28ms Memory 13.1mb

Algorithm:
Greedy: track the farthest reachable position (current). For each position i, if i > current, return False (can't reach i). Otherwise, update current = max(current, i + nums[i]). If current >= end, return True. This checks if we can reach the end by always maximizing reach.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        current = 0
        end = len(nums) - 1
        
        
        for i in range(len(nums)):

            if i > current:
                return False
            
            current = max(current, i + nums[i])
        
        
            if current >= end:
                return True

        return False