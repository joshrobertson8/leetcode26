"""
LeetCode: 2026 01 04 23.29.56 Accepted Runtime 5ms Memory 17.3MB

Algorithm:
Greedy: sort weights in ascending order. Start with basket capacity 5000. Iterate through sorted weights, subtracting each weight from basket. If basket remains non-negative, increment count. If basket becomes negative, stop (can't fit more). This maximizes count by always taking the lightest available apples first.

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