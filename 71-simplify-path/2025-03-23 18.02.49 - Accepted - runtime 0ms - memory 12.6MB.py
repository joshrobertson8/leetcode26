"""
LeetCode: 2025 03 23 18.02.49 Accepted Runtime 0ms Memory 12.6mb

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
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