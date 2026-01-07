"""
LeetCode: 2024 10 03 02.23.28 Accepted Runtime 16ms Memory 11.7mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution(object):
    def isValid(self, s):
        
        match = []
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            
            if char in bracket_map.values():
                match.append(char)
            
            elif char in bracket_map.keys():
                if match == [] or match.pop() != bracket_map[char]:
                    return False
        
        return len(match) == 0