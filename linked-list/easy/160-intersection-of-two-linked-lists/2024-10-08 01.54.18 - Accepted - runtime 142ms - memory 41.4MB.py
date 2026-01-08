"""
LeetCode: 2024 10 08 01.54.18 Accepted Runtime 142ms Memory 41.4MB

Algorithm:
Two-pointer technique: traverse both lists simultaneously. When one pointer reaches end, switch it to the other list's head. When both pointers meet (pA == pB), that's the intersection. If no intersection, both become None simultaneously. This handles different list lengths.

Time Complexity: O(n)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):

        pA = headA
        pB = headB

        while pA != pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next

        return pB