"""
LeetCode: 2024 10 08 01.54.22 Accepted Runtime 127ms Memory 41.5MB

Algorithm:
Two-pointer technique: use pointers pA and pB starting at headA and headB. When a pointer reaches the end of its list, switch it to the head of the other list. Continue until both pointers meet (pA == pB). If lists intersect, they will meet at the intersection node. If not, both will be None. This works because both pointers traverse the same total distance (lengthA + lengthB), ensuring they meet at the intersection if it exists.

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