"""
LeetCode: 2025 12 29 17.32.28 Accepted Runtime 202ms Memory 19MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        numOfBananas = sum(piles)
        res = 0

        def canFinish(speed):
            time = 0

            for i in range(len(piles)):
                time += math.ceil(piles[i] / speed)

            return time <= h

        low, high = 1, max(piles)

        while low <= high:
            middle = (low + high) // 2

            if canFinish(middle):
                res = middle
                high = middle - 1
            
            else: 
                low = middle + 1
        return res