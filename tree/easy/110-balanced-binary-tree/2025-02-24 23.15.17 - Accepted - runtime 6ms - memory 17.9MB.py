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