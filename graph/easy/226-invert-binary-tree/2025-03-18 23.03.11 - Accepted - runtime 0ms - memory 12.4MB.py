"""
LeetCode: 2025 03 18 23.03.11 Accepted Runtime 0ms Memory 12.4MB

Algorithm:
Recursive DFS: if root is None, return None. Swap left and right children of current node. Recursively invert right and left subtrees. Return the root. This inverts the entire tree by swapping children at each level.

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
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None

        temp = root.right
        root.right = root.left
        root.left = temp

        self.invertTree(root.right)
        self.invertTree(root.left)
        
        return root