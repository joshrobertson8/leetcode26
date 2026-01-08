"""
LeetCode: 2025 07 02 08.18.02 Accepted Runtime 22ms Memory 16.1mb

Algorithm:
For each word, sort its characters to create a canonical form. Use sorted word as key in hash map. Group words with the same sorted form together. Anagrams will have the same sorted form. Return all groups (values of the map).

Time Complexity: O(n log n)
Space Complexity: O(n)
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

        return master.values()