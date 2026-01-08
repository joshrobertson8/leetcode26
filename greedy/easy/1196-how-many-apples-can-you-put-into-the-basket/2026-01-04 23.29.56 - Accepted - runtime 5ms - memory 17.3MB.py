"""
LeetCode: 2026 01 04 23.29.56 Accepted Runtime 5ms Memory 17.3MB

Algorithm:
Sort the input first. Use sliding window to track a valid subarray.

Time Complexity: O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        
        weight.sort()
        basket = 5000
        count = 0

        for apple in weight:

            basket -= apple
            if basket >= 0:
                count += 1
            else:
                break
        return count