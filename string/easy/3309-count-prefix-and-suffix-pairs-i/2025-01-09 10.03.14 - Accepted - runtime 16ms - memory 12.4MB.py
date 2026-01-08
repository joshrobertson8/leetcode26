"""
LeetCode: 2025 01 09 10.03.14 Accepted Runtime 16ms Memory 12.4mb

Algorithm:
Nested loop comparison: for each pair (i, j) where i < j, check if words[i] is both prefix and suffix of words[j]. Check prefix: str2[:len(str1)] == str1. Check suffix: str2[-len(str1):] == str1. If both conditions true, increment count. This counts how many earlier words are both prefix and suffix of later words.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        count = 0 

        for i in range(len(words)):
            
            for j in range(i + 1, len(words)):

                str1 = words[i]
                str2 = words[j]

                pre = str2[:len(str1)] == str1
                suf = str2[-len(str1):] == str1

                if pre and suf:
                    count += 1
        return count