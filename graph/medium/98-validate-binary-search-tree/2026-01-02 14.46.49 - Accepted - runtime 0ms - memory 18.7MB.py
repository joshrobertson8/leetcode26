"""
LeetCode: 2026 01 02 14.46.49 Accepted Runtime 0ms Memory 18.7MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(?)
Space Complexity: O(?)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(cur, low=-math.inf, high=math.inf):
            if not cur:
                return True

            if cur.val <= low or cur.val >= high:
                return False

            return validate(cur.right, cur.val, high) and validate(cur.left, low, cur.val)
        
        return validate(root)