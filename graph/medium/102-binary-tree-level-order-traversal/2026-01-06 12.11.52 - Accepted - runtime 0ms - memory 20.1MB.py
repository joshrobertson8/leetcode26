"""
LeetCode: 2026 01 06 12.11.52 Accepted Runtime 0ms Memory 20.1MB

Algorithm:
Two pointers approach. DFS traversal.

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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []


        def dfs(level, node):
            if not node:
                return

            if level == len(res):
                res.append([])

            res[level].append(node.val)
            
            dfs(level + 1, node.left)
            dfs(level + 1, node.right)


        dfs(0, root)
        return res