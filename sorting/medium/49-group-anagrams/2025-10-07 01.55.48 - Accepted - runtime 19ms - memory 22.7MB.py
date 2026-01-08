"""
LeetCode: 2025 10 07 01.55.48 Accepted Runtime 19ms Memory 22.7MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
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