"""
LeetCode: 2025 01 16 10.01.13 Accepted Runtime 63ms Memory 12.8mb

Algorithm:
Character frequency analysis: count frequency of each character. Key insight: a palindrome can have at most one character with odd frequency. Count characters with odd frequencies (odd_freq). If string length < k, impossible to form k palindromes. If odd_freq > k, impossible (need at least one palindrome per odd-frequency character). Otherwise possible. This determines if string can be partitioned into k palindromes.

Time Complexity: O(n)
Space Complexity: O(n)
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