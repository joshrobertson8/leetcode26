"""
LeetCode: 2024 10 09 15.27.52 Accepted Runtime 23ms Memory 11.6mb

Algorithm:
Stack-based approach.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def isValid(self, s):
        
        bracket_map = {')': '(', '}': '{', ']': '['}
        result = []

        for i in s:

            if i in bracket_map.values():
                result.append(i)

            elif i in bracket_map.keys():
                if result == [] or result.pop() != bracket_map[i]:
                    return False
        return len(result) == 0