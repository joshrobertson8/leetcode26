"""
LeetCode: 2025 12 16 15.55.46 Accepted Runtime 6ms Memory 20.1MB

Algorithm:
Sort start and end times separately. Use two pointers: s for start times, e for end times. When start[s] < end[e], a meeting starts (increment count). When start[s] >= end[e], a meeting ends (decrement count). Track maximum count (maxCount) which represents maximum concurrent meetings needed.

Time Complexity: O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        curCount, maxCount = 0, 0

        start = sorted([s[0] for s in intervals])
        end = sorted([e[1] for e in intervals])


        s, e = 0, 0                # pointers

        while s < len(intervals):
            if start[s] < end[e]: 
                curCount += 1
                s += 1

            elif start[s] >= end[e]: 
                curCount -= 1
                e += 1

            maxCount = max(maxCount, curCount)

        return maxCount