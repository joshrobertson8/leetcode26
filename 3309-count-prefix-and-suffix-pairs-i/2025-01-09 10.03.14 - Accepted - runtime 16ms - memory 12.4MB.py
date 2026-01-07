"""
LeetCode: 2025 01 09 10.03.14 Accepted Runtime 16ms Memory 12.4mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
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