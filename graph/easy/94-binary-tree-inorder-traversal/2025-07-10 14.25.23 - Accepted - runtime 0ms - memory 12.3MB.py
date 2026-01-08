"""
LeetCode: 2025 07 10 14.25.23 Accepted Runtime 0ms Memory 12.3MB

Algorithm:
Two pointers approach.

Time Complexity: O(log n)
Space Complexity: O(1)
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