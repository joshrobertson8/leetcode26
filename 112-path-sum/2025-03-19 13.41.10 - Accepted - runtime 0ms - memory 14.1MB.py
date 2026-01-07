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
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

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