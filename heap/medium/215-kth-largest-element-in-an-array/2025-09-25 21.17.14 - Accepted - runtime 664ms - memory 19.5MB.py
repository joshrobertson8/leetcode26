"""
LeetCode: 2025 09 25 21.17.14 Accepted Runtime 664ms Memory 19.5mb

Algorithm:
Maintain a min-heap of size k. For each number, push to heap. If heap size exceeds k, pop the smallest element. This keeps the k largest elements. The root of the heap (heap[0]) is the kth largest element. Python's heapq is a min-heap, so smallest elements are popped.

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