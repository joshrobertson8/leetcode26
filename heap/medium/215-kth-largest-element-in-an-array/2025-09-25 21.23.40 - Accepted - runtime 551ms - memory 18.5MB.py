"""
LeetCode: 2025 09 25 21.23.40 Accepted Runtime 551ms Memory 18.5mb

Algorithm:
Use a heap to always get the smallest/largest element.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        
        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)

        return nums[0]