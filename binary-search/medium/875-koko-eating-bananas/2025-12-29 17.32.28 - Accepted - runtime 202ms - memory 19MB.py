"""
LeetCode: 2025 12 29 17.32.28 Accepted Runtime 202ms Memory 19MB

Algorithm:
Binary search on the answer (eating speed). Define canFinish(speed) that calculates total time needed: sum of ceil(pile/speed) for all piles. Binary search between 1 and max(piles). If canFinish(mid), try slower speeds (high = mid - 1). Otherwise, try faster speeds (low = mid + 1). Return the minimum valid speed.

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