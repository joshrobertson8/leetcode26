"""
LeetCode: 2025 07 11 11.43.35 Accepted Runtime 236ms Memory 17.1mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def totalFruit(self, fruits):
        basket = {}
        left = 0
        max_len = 0

        for right in range(len(fruits)):
            fruit = fruits[right]
            basket[fruit] = basket.get(fruit, 0) + 1

            while len(basket) > 2:
                left_fruit = fruits[left]
                basket[left_fruit] -= 1
                if basket[left_fruit] == 0:
                    del basket[left_fruit]
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len