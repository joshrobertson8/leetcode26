"""
LeetCode: 2025 03 21 23.08.10 Accepted Runtime 7ms Memory 15.2mb

Algorithm:
Bijection mapping: maintain two hash maps - s_map maps characters from s to t, t_map maps characters from t to s. For each character pair (x, y), if x already mapped, verify it maps to y. If y already mapped, verify it maps to x. This ensures one-to-one mapping (bijection) - each character in s maps to exactly one character in t, and vice versa. If any violation found, strings are not isomorphic.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_map = {}
        t_map = {}

        for x, y in zip(s, t):

            if x in s_map:
                if s_map[x] != y:
                    return False
            else:
                s_map[x] = y 

            if y in t_map:
                if t_map[y] != x:
                    return False
            else:
                t_map[y] = x
        return True