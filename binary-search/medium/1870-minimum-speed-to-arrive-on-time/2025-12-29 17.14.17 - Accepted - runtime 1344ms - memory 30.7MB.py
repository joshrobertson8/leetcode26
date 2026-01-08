"""
LeetCode: 2025 12 29 17.14.17 Accepted Runtime 1344ms Memory 30.7MB

Algorithm:
Binary search on the answer (train speed). First check if it's possible: if hour < n-1, return -1. Define canFinish(speed) that calculates total time: sum of ceil(dist[i]/speed) for first n-1 segments, plus dist[n-1]/speed for the last segment. Binary search between 1 and 10^7. If canFinish(mid), try slower speeds. Otherwise, try faster speeds. Return the minimum valid speed.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)

        if hour < n - 1: 
            return -1 

        def canFinish(speed: float) -> bool:
            time = 0.0

            for i in range(n - 1):
                time += math.ceil(dist[i] / speed)

            time += dist[n - 1] / speed

            return time <= hour

        low, high = 1, 10**7
        res = -1

        while low <= high:
            mid = (low + high) // 2
            
            if canFinish(mid):
                res = mid
                high = mid - 1

            else:
                low = mid + 1
        return res