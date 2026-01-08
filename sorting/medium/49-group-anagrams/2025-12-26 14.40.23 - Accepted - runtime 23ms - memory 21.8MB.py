"""
LeetCode: 2025 12 26 14.40.23 Accepted Runtime 23ms Memory 21.8MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(n²)
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