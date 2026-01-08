"""
LeetCode: 2025 07 10 14.25.23 Accepted Runtime 0ms Memory 12.3MB

Algorithm:
Recursive inorder traversal: if root is None, return. Recursively traverse left subtree, append root.val to result, then recursively traverse right subtree. This visits nodes in left-root-right order.

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
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []

        def inOrder(root):

            if root is None:
                return 
            
            inOrder(root.left)
            result.append(root.val)
            inOrder(root.right)

        inOrder(root)
        return result