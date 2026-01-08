"""
LeetCode: 2025 02 24 23.22.21 Accepted Runtime 4ms Memory 15.6MB

Algorithm:
TODO: Describe your approach here

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
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0 

        else:
            r_height = self.maxDepth(root.right)
            l_height = self.maxDepth(root.left)

        return 1 + max(r_height, l_height)