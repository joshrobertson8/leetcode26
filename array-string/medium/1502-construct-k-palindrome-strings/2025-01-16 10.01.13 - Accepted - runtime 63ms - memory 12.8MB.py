"""
LeetCode: 2025 01 16 10.01.13 Accepted Runtime 63ms Memory 12.8mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        freq = {}
        odd_freq = 0

        if len(s) < k:
            return False

        for char in s:
            if char in freq:
                freq[char] +=1 
            else:
                freq[char] = 1


        for value in freq.values():
            if value % 2 != 0:
                odd_freq += 1
        
        if odd_freq > k:
            return False

        return True