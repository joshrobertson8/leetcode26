"""
LeetCode: 2025 08 05 14.19.01 Accepted Runtime 29ms Memory 12.3mb

Algorithm:
Use nested loops to check all pairs.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        res = 0 
        idx = 0
        n = len(baskets)

        for fruit in fruits:
            unset = 1

            for j in range(n):

                if fruit <= baskets[j]: 
                    unset = 0
                    baskets[j] = 0
                    break
            res += unset
                
        return res