"""
LeetCode: 2025 01 09 10.11.10 Accepted Runtime 0ms Memory 12.5mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        count = 0

        for i in words:
            if i.startswith(pref):
                count += 1

        return count