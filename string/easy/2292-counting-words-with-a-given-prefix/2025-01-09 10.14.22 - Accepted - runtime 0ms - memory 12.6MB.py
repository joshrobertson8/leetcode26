"""
LeetCode: 2025 01 09 10.14.22 Accepted Runtime 0ms Memory 12.6mb

Algorithm:
Prefix matching with slice: iterate through each word. Check if prefix of word (word[:len(pref)]) equals pref. If true, increment count. Return total count of words that have pref as prefix. This counts how many words start with the given prefix string using slice comparison instead of startswith().

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
            pre = i[:len(pref)] == pref

            if pre:
                count += 1

        return count