"""
LeetCode: 2025 07 11 11.53.09 Accepted Runtime 183ms Memory 16.4MB

Algorithm:
Sliding window with hash map: track fruit types in basket map. Expand window by adding fruits[right]. If basket has more than 2 types, shrink from left (decrement count, delete if zero, increment base). Track maximum window size (idx - base + 1). This finds longest subarray with at most 2 distinct fruit types.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        basket = {}
        base = 0 
        maxLen  = 0

        for idx, fruit in enumerate(fruits):

            basket[fruit] = basket.get(fruit, 0) + 1

            if len(basket) > 2:
                basket[fruits[base]] -= 1

                if basket[fruits[base]] == 0:
                    del basket[fruits[base]]

                base += 1

            maxLen = max(maxLen, idx - base + 1)

        return maxLen