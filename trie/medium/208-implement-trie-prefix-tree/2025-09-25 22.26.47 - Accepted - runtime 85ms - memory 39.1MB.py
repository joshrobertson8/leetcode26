"""
LeetCode: 2025 09 25 22.26.47 Accepted Runtime 85ms Memory 39.1MB

Algorithm:
Trie data structure: TrieNode has children dictionary and finished flag. insert() traverses/creates path character by character, marks end with finished=True. search() traverses path, returns True only if finished=True at end. startsWith() traverses path, returns True if path exists (regardless of finished flag). This enables efficient prefix matching and word lookup.

Time Complexity: O(m) for insert/search/startsWith where m is word/prefix length.
Space Complexity: O(ALPHABET_SIZE * N * M) where N is number of words and M is average word length.
"""
class TrieNode(): 
    def __init__(self):
        self.children = {}
        self.finished = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self.root

        for char in word: 
            if char not in cur.children: 
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        
        cur.finished = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cur = self.root

        for char in word: 
            if char not in cur.children: 
                return False
            cur = cur.children[char]

        return cur.finished

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        cur = self.root

        for char in prefix: 
            if char not in cur.children: 
                return False
            cur = cur.children[char]

        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)