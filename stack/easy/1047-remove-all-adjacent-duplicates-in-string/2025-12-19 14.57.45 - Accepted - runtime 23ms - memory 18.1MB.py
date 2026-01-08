"""
LeetCode: 2025 12 19 14.57.45 Accepted Runtime 23ms Memory 18.1MB

Algorithm:
Use a stack.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        stack = []

        for i in range(len(s)): 

            if stack and stack[-1] == s[i]: 
                stack.pop()

            else: 
                stack.append(s[i])

        return "".join(stack)