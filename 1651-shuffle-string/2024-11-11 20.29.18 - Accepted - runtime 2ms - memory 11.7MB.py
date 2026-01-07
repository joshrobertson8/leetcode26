"""
LeetCode: 2024 11 11 20.29.18 Accepted Runtime 2ms Memory 11.7mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        shuffled = {}
        
        # Populate the dictionary with indices as keys and characters as values
        for i in range(len(s)):
            shuffled[indices[i]] = s[i]
        
        # Sort keys and concatenate characters in the sorted order of indices
        res = ""
        for i in sorted(shuffled.keys()):
            res += shuffled[i]
        
        return res