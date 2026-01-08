"""
LeetCode: 2025 03 19 13.41.11 Accepted Runtime 0ms Memory 14.1MB

Algorithm:
Recursive DFS: if root is None, return False. If it's a leaf (no children), check if targetSum equals root.val. Otherwise, subtract root.val from targetSum and recursively check left or right subtree. Return True if either subtree has a path with the remaining sum.

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
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
 

        if not root:
            return False

        if not root.left and not root.right:
            return targetSum == root.val
        
        targetSum -= root.val
        
        return self.hasPathSum(root.right, targetSum) or self.hasPathSum(root.left, targetSum)