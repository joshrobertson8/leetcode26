"""
LeetCode: 2025 07 11 11.44.30 Accepted Runtime 140ms Memory 16.4MB

Algorithm:
Sliding window with hash map: track fruit types in basket map. Expand window by adding fruits[right]. If basket has more than 2 types, shrink from left (decrement count, delete if zero, increment left). Return final window size (right - left + 1). This finds longest subarray with at most 2 distinct fruit types.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def totalFruit(self, fruits):
        # Hash map 'basket' to store the types of fruits.
        basket = {}
        left = 0
        
        # Add fruit from the right index (right) of the window.
        for right, fruit in enumerate(fruits):
            basket[fruit] = basket.get(fruit, 0) + 1

            # If the current window has more than 2 types of fruit,
            # we remove one fruit from the left index (left) of the window.
            if len(basket) > 2:
                basket[fruits[left]] -= 1

                # If the number of fruits[left] is 0, remove it from the basket.
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1
        
        # Once we finish the iteration, the indexes left and right 
        # stands for the longest valid subarray we encountered.
        return right - left + 1