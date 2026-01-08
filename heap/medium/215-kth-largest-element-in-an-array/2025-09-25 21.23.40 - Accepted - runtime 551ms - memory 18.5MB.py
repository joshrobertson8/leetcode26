"""
LeetCode: 2025 09 25 21.23.40 Accepted Runtime 551ms Memory 18.5mb

Algorithm:
Convert array to heap in-place using heapify. Pop elements until heap size equals k. The root (nums[0]) is now the kth largest element. This modifies the original array but is more space-efficient.

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