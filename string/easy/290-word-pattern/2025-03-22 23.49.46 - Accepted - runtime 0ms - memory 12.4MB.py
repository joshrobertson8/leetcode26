"""
LeetCode: 2025 03 22 23.49.46 Accepted Runtime 0ms Memory 12.4mb

Algorithm:
Use a hash table to store seen elements for O(1) lookup. Dynamic programming with memoization.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        mapp = {}
        words = []
        temp = ""

        for char in s:
            if char != " ":
                temp += char
            else:
                if temp:
                    words.append(temp)
                    temp = ""

        if temp:
            words.append(temp)

        if len(pattern) != len(words):
            return False

        for i in range(len(pattern)):
            char = pattern[i]
            word = words[i]

            if char in mapp:
                if mapp[char] != word:
                    return False
            else:
                if word in mapp.values():
                    return False
                mapp[char] = word

        return True