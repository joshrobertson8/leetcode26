"""
LeetCode: 2025 03 09 22.08.14 Accepted Runtime 19ms Memory 20.2mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l = 0 
        r = 0
        cur_sum = 0 
        res = float('inf')   

        for num in range(len(nums)):
            cur_sum += nums[r]
            r += 1

            while cur_sum >= target:
                res = min(res, r - l)
                cur_sum -= nums[l]
                l += 1
        
        return res if res != float('inf') else 0