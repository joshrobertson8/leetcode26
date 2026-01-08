"""
LeetCode: 2025 08 04 17.34.14 Accepted Runtime 215ms Memory 16.4MB

Algorithm:
Sliding window with hash map: track fruit types in basket map. Expand window by adding fruits[right]. While basket has more than 2 types, shrink from left (decrement count, delete if zero, increment base). Track maximum window size (idx - base + 1). This finds longest subarray with at most 2 distinct fruit types.

Time Complexity: O(n^2)
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
        maxWindow = 0

        for idx, fruit in enumerate(fruits):
            basket[fruit] = basket.get(fruit, 0) + 1

            while len(basket) > 2:
                leftFruit = fruits[base]

                basket[leftFruit] -= 1

                if basket[leftFruit] == 0:
                    del basket[leftFruit]

                base += 1

            maxWindow = max(maxWindow, idx - base + 1)

        return maxWindow
            