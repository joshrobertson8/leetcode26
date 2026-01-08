"""
LeetCode: 2025 01 16 09.57.29 Accepted Runtime 63ms Memory 12.9MB

Algorithm:
Count character frequencies. A palindrome can have at most one character with odd frequency. Count how many characters have odd frequencies (odd_freq). To form k palindromes, we need at least k characters (len(s) >= k) and at most k characters with odd frequencies (odd_freq <= k). Return True if both conditions hold.

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