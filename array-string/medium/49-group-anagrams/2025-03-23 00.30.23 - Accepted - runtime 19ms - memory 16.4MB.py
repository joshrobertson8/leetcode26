"""
LeetCode: 2025 03 23 00.30.23 Accepted Runtime 19ms Memory 16.4mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        master = {}
        
        for word in strs:
            
            sorted_word = ''.join(sorted(word))
            
            if sorted_word not in master:
                master[sorted_word] = []
                master[sorted_word].append(word)
            else:
                master[sorted_word].append(word)

        return list(master.values())