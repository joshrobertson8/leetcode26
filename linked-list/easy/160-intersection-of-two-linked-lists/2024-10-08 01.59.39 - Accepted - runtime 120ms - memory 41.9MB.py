"""
LeetCode: 2024 10 08 01.59.39 Accepted Runtime 120ms Memory 41.9MB

Algorithm:
Hash set approach: traverse list B and store all nodes in a set. Then traverse list A, checking if each node exists in the set. The first node found in the set is the intersection point. This uses O(n) space but provides O(1) lookup for intersection detection.

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

        map = set()

        while headB:
            map.add(headB)
            headB = headB.next

        while headA:
            if headA in map:
                return headA
            headA = headA.next
        return None