"""
LeetCode: 2024 10 09 15.27.52 Accepted Runtime 23ms Memory 11.6mb

Algorithm:
Use stack to match brackets: map closing brackets to opening brackets. For opening brackets, push to stack. For closing brackets, if stack is empty or top doesn't match, return False. Otherwise pop. After processing, stack must be empty for valid parentheses.

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