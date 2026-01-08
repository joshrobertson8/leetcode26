"""
LeetCode: 2026 01 04 23.35.35 Accepted Runtime 3ms Memory 17.4MB

Algorithm:
TODO: Describe your approach here

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