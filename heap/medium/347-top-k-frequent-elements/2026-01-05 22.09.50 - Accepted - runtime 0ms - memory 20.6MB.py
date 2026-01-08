"""
LeetCode: 2026 01 05 22.09.50 Accepted Runtime 0ms Memory 20.6MB

Algorithm:
Use Counter to count frequencies. Maintain a min-heap of size k containing (frequency, value) pairs. For each number, push to heap. If heap size exceeds k, pop the smallest frequency. This keeps the k most frequent elements. Extract values from the final heap.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List
import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequencies
        freq = Counter(nums)

        # Min-heap of (frequency, value)
        heap = []

        for num, count in freq.items():
            heapq.heappush(heap, (count, num))

            # Keep heap size at most k
            if len(heap) > k:
                heapq.heappop(heap)

        # Extract values from heap
        return [num for count, num in heap]
