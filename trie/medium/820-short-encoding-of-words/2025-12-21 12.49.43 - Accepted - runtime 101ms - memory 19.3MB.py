"""
LeetCode: 2025 12 21 12.49.43 Accepted Runtime 101ms Memory 19.3MB

Algorithm:
Build reverse trie: insert reversed words into trie (so suffixes become prefixes). Use DFS to traverse trie: if node is end of word (end=True) and has no children (leaf), add depth+1 to total (depth for word length, +1 for '#' separator). This finds minimum encoding length by identifying words that are not suffixes of other words.

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

            