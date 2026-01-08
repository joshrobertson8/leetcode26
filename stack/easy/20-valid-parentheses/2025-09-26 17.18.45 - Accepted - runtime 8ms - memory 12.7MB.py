"""
LeetCode: 2025 09 26 17.18.45 Accepted Runtime 8ms Memory 12.7mb

Algorithm:
Stack-based approach.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def isValid(self, s):
        

        stack = []

        openToClose = {')':'(', '}':'{', ']':'['}

        for char in s: 
            
            if char in openToClose.values():
                stack.append(char)

            elif char in openToClose.keys():
                if not stack or stack[-1] != openToClose[char]: 
                    return False
                
                stack.pop()

        return len(stack) == 0