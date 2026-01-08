"""
LeetCode: 2025 02 24 23.15.18 Accepted Runtime 6ms Memory 17.9MB

Algorithm:
Recursive DFS with early termination: compute height of each subtree. If any subtree is unbalanced (returns -1), propagate -1 upward. If heights differ by more than 1, return -1. Otherwise return height (1 + max of left/right). Tree is balanced if final result is not -1.

Time Complexity: O(n)
Space Complexity: O(n)
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(root):

            if not root:
                return 0

            r_height = dfs(root.right)

            if r_height == -1: 
                return -1 

            l_height = dfs(root.left)
            
            if l_height == -1:
                return -1 

            if abs(l_height - r_height) > 1:
                return -1

            return 1 + max(l_height, r_height)

        return dfs(root) != -1