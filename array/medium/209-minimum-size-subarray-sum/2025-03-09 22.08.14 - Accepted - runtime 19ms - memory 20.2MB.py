"""
LeetCode: 2025 03 09 22.08.14 Accepted Runtime 19ms Memory 20.2mb

Algorithm:
Use sliding window technique with two pointers. Expand the window by moving the right pointer and adding elements to the current sum. When the sum reaches or exceeds the target, try to shrink the window from the left while maintaining the sum >= target, updating the minimum length. Track the minimum subarray length found.

Time Complexity: O(n^2)
Space Complexity: O(1)
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