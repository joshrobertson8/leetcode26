"""
LeetCode: 2025 08 04 16.27.11 Accepted Runtime 180ms Memory 16.5MB

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
        left = 0
        max_fruits = 0

        for right, fruit in enumerate(fruits):
            # Add fruit
            basket[fruit] = basket.get(fruit, 0) + 1

            # Try to fix if too many types
            if len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1

            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits
