"""
LeetCode: 2025 12 26 14.40.23 Accepted Runtime 23ms Memory 21.8MB

Algorithm:
Process the input directly.

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = {}

        for word in strs:
            mapper = [0] * 26

            for char in word: 
                mapper[ord(char) - ord('a')] += 1

            if tuple(mapper) not in res:
                res[tuple(mapper)] = []
            
            res[tuple(mapper)].append(word)

        return list(res.values())