"""
LeetCode: 2025 02 28 14.02.45 Accepted Runtime 4ms Memory 15.1MB

Algorithm:
Recursive DFS: if root is None, return 0. Otherwise, recursively compute depth of left and right subtrees. Return 1 (current node) plus the maximum of left and right depths. This finds the longest path from root to any leaf.

Time Complexity: O(1)
Space Complexity: O(1)
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)
