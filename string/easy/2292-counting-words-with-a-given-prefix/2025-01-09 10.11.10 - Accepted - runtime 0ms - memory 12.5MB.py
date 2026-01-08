"""
LeetCode: 2025 01 09 10.11.10 Accepted Runtime 0ms Memory 12.5mb

Algorithm:
Prefix matching: iterate through each word in words. Use startswith() method to check if word begins with pref. If true, increment count. Return total count of words that have pref as prefix. This counts how many words start with the given prefix string.

Time Complexity: O(n)
Space Complexity: O(1)
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