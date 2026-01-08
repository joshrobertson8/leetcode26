"""
LeetCode: 2025 03 23 18.02.49 Accepted Runtime 0ms Memory 12.6mb

Algorithm:
Use stack to build simplified path: split path by '/'. For each part, if '..', pop from stack (go up one directory). If '.' or empty, skip. Otherwise push to stack. Finally join stack with '/' and prepend '/'. This handles directory navigation and simplifies the path.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        
        stack = []

        for i in path.split("/"):

            if i == "..":
                if stack:
                    stack.pop()
            elif i == ".":
                continue
            elif not i:
                continue
            else:
                stack.append(i)
        return "/"+ '/'.join(stack)