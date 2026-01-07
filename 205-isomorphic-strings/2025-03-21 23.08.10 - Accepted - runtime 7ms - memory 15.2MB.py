"""
LeetCode: 2025 03 21 23.08.10 Accepted Runtime 7ms Memory 15.2mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
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