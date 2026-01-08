"""
LeetCode: 2025 12 27 15.50.31 Accepted Runtime 7ms Memory 19.4MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start, end = [], []

        for s, e in intervals:
            start.append(s)
            end.append(e)

        start.sort()
        end.sort()

        s = e = 0
        count = maxCount = 0

        while s < len(start):
            if start[s] < end[e]:
                count += 1
                maxCount = max(maxCount, count)
                s += 1
            else:
                count -= 1
                e += 1

        return maxCount
