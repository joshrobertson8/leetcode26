"""
LeetCode: 2025 12 19 15.57.21 Accepted Runtime 1350ms Memory 65.2MB

Algorithm:
Trie with wildcard search: TrieNode has children dictionary and end flag. addWord() inserts word normally. search() uses DFS: if character is '.', recursively search all children. Otherwise, traverse to specific child. Return True if path exists and ends at word boundary (end=True). This enables pattern matching with '.' as wildcard.

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

class TrieNode: 

    def __init__(self): 
        self.children = {}
        self.end = False


class WordDictionary:

    def __init__(self):
        self.base = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.base

        for ch in word: 
            if ch not in cur.children: 
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.end = True
            

    def search(self, word: str) -> bool:
        
        def dfs(idx, base): 
            cur = base

            for i in range(idx, len(word)): 
                ch = word[i]

                if ch == ".": 
                    for child in cur.children.values(): 
                        if dfs(i + 1, child): 
                            return True
                    return False

                else: 
                    if ch not in cur.children: 
                        return False
                    cur = cur.children[ch]
            return cur.end

        return dfs(0, self.base)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)