"""
LeetCode: 2024 10 08 01.59.39 Accepted Runtime 120ms Memory 41.9MB

Algorithm:
Use a set for O(1) lookup. Use two pointers moving toward each other.

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