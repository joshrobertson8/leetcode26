"""
LeetCode: 2025 12 26 14.40.23 Accepted Runtime 23ms Memory 21.8MB

Algorithm:
Use character frequency array as key: for each word, create 26-element array counting character frequencies. Convert to tuple and use as hash map key. Group words with same frequency tuple together. Anagrams will have identical frequency arrays. Return grouped words.

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