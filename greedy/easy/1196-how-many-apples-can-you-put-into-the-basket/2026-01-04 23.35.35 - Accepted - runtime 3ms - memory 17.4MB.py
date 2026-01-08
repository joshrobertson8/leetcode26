"""
LeetCode: 2026 01 04 23.35.35 Accepted Runtime 3ms Memory 17.4MB

Algorithm:
Greedy using min-heap: heapify the weight list. While heap is not empty and adding the smallest weight doesn't exceed 5000, pop the smallest weight, add to expense, and increment apple count. This maximizes count by always taking the lightest available apples first.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        
        heapq.heapify(weight)

        apples = expense = 0

        while weight and expense + weight[0] <= 5000:
            

            expense += heapq.heappop(weight)
            apples += 1

        return apples