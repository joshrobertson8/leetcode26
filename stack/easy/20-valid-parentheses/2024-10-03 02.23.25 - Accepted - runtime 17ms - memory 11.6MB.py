"""
LeetCode: 2024 10 03 02.23.25 Accepted Runtime 17ms Memory 11.6mb

Algorithm:
Use stack to match brackets: map closing brackets to opening brackets. For opening brackets, push to stack. For closing brackets, if stack is empty or top doesn't match, return False. Otherwise pop. After processing, stack must be empty for valid parentheses.

Time Complexity: O(n)
Space Complexity: O(n)
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