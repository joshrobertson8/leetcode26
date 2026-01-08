"""
LeetCode: 2025 12 24 09.49.01 Accepted Runtime 0ms Memory 17.5MB

Algorithm:
Use a stack.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) == 1:
            return False

        bank = {
            ")":"(",
            "}":"{",
            "]":"[" 
        } 

        for ch in s: 
            if ch in bank.values():
                stack.append(ch)

            elif ch in bank.keys(): 
                if stack and stack[-1] == bank[ch]:
                    stack.pop()
                else: 
                    return False
        return len(stack) == 0