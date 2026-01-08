"""
LeetCode: 2026 01 02 14.46.49 Accepted Runtime 0ms Memory 18.7MB

Algorithm:
Recursive validation with bounds: each node must be within (low, high) range. Root can be any value. For left child, upper bound becomes parent's value. For right child, lower bound becomes parent's value. If any node violates its bounds, return False. Recursively validate left and right subtrees with updated bounds.

Time Complexity: O(n)
Space Complexity: O(n)
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