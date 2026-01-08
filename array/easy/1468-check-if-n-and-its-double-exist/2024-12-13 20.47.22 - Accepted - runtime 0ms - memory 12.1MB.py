"""
LeetCode: 2024 12 13 20.47.22 Accepted Runtime 0ms Memory 12.1mb

Algorithm:
Use a set for O(1) lookup.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        seen = set()

        for i in arr:
            if 2 * i in seen or ( i % 2 == 0 and i // 2 in seen):
                return True
            else:
                seen.add(i)

        return False