"""
LeetCode: 2026 01 04 23.21.30 Accepted Runtime 4ms Memory 17.3MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        words = defaultdict(int)
        
        s1Words = s1.split()
        s2Words = s2.split()

        for word in s1Words:
            words[word] += 1

        for word in s2Words:
            words[word] += 1

        return [word for word in words if words[word] == 1]