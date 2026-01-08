"""
LeetCode: 2024 11 13 22.18.04 Accepted Runtime 131ms Memory 41.8MB

Algorithm:
Hash set approach: traverse list A and store all nodes in a set. Then traverse list B, checking if each node exists in the set. The first node found in the set is the intersection point. This uses O(n) space but provides O(1) lookup for intersection detection.

Time Complexity: O(n)
Space Complexity: O(n)
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):

        nodes_in_A = set()

        while headA is not None:
            nodes_in_A.add(headA)
            headA = headA.next

        while headB is not None:
            # if we find the node pointed to by headA,
            # in our set containing nodes of B, then return the node
            if headB in nodes_in_A:
                return headB
            headB = headB.next

        return None