"""
LeetCode: 2025 09 25 21.17.14 Accepted Runtime 664ms Memory 19.5mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = [] 

        for num in nums: 
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]