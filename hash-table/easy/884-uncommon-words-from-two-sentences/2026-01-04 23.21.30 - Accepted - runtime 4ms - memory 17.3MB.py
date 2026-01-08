"""
LeetCode: 2026 01 04 23.21.30 Accepted Runtime 4ms Memory 17.3MB

Algorithm:
Split both sentences into words. Build frequency map counting occurrences of each word across both sentences. Return all words that appear exactly once (frequency == 1). These are words that appear in only one sentence and only once.

Time Complexity: O(n)
Space Complexity: O(n)
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