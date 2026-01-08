"""
LeetCode: 2026 01 02 14.25.09 Accepted Runtime 0ms Memory 17.3MB

Algorithm:
Recursively process each element.

Time Complexity: O(1)
Space Complexity: O(1)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        cur = root

        if not cur:
            return None

        temp = cur.left
        cur.left = cur.right
        cur.right = temp

        self.invertTree(cur.left)
        self.invertTree(cur.right)

        return cur
        