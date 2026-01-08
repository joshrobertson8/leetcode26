"""
LeetCode: 2025 03 22 23.49.46 Accepted Runtime 0ms Memory 12.4mb

Algorithm:
Bijection mapping: split string into words. Check if pattern length matches word count. Build character-to-word mapping: for each pattern character and corresponding word, if character already mapped, verify it maps to same word. If character not mapped, check word isn't already mapped to another character (bijection requirement). If all mappings are valid, pattern matches.

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