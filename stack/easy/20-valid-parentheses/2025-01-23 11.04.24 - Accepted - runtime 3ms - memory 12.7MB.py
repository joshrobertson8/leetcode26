"""
LeetCode: 2025 01 23 11.04.24 Accepted Runtime 3ms Memory 12.7mb

Algorithm:
Stack-based approach.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def isValid(self, s):
        
        stack = []

        Map = {"}": "{", "]": "[", ")":"("}

        for i in s:

            if i in Map:
                if stack and stack[-1] == Map[i]:
                    stack.pop()

                else:
                    return False
            else:
                stack.append(i)

        return len(stack) == 0