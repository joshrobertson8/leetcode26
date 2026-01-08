"""
LeetCode: 2025 09 25 21.30.53 Accepted Runtime 659ms Memory 19.6mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(n)
Space Complexity: O(n)
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