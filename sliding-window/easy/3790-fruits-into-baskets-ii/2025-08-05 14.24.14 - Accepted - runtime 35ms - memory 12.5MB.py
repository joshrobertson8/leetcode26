"""
LeetCode: 2025 08 05 14.24.14 Accepted Runtime 35ms Memory 12.5mb

Algorithm:
Greedy matching: for each fruit, try to place it in the first basket that can fit it (fruit <= baskets[j]). If placed successfully, mark basket as used (set to 0) and break. If no basket can fit the fruit, increment unplaced count. This minimizes unplaced fruits by always trying to place each fruit.

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