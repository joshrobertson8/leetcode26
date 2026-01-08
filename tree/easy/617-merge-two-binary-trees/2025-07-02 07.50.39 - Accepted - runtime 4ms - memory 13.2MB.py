"""
LeetCode #0: , left=none, right=none):

Problem:
Definition for a binary tree node.
class TreeNode(object):
def __init__(self, val=0, left=None, right=None):
self.val = val
self.left = left
self.right = right

Algorithm:
Two pointers approach.

Time Complexity: O(1)
Space Complexity: O(1)
"""

class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root1 and not root2:
            return None
        
        if root1 is None:
            return root2
        
        if root2 is None:
            return root1
        
        
        merged = TreeNode(root1.val + root2.val)
        
        merged.left = self.mergeTrees(root1.left, root2.left)
        merged.right =  self.mergeTrees(root1.right, root2.right)
        
        return merged