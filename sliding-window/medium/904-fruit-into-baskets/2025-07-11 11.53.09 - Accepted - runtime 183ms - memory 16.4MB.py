"""
LeetCode: 2025 07 11 11.53.09 Accepted Runtime 183ms Memory 16.4MB

Algorithm:
TODO: Describe your approach here

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