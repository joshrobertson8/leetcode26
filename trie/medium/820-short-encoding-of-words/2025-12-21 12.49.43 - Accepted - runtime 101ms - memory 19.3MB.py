"""
LeetCode: 2025 12 21 12.49.43 Accepted Runtime 101ms Memory 19.3MB

Algorithm:
Use a set for O(1) lookup. Use a recursive helper function to explore all possibilities.

Time Complexity: O(n^2)
Space Complexity: O(n)
"""


class TrieNode: 

    def __init__(self): 
        self.children = {}
        self.end = False

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        root = TrieNode()
        words = set(words)

        for word in words: 
            curr = root
            for ch in reversed(word): 
                if ch not in curr.children: 
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            curr.end = True

        total = 0

        def dfs(node, depth): 
            nonlocal total

            if node.end and not node.children:
                total += depth + 1                                      # +1 for end char (#)
            
            for child in node.children.values():
                dfs(child, depth + 1)
        
        dfs(root, 0)
        return total

            