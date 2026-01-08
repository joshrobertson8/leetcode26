"""
LeetCode: 2025 10 07 01.55.48 Accepted Runtime 19ms Memory 22.7MB

Algorithm:
Use character frequency array as key: for each word, create 26-element count array counting character frequencies. Convert to tuple and use as hash map key (with defaultdict). Group words with same frequency tuple together. Anagrams will have identical frequency arrays. Return grouped words.

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)


        for word in strs:

            count = [0] * 26

            for c in word: 
                count[ord(c) - ord('a')] += 1

            res[tuple(count)].append(word)

        return list(res.values())