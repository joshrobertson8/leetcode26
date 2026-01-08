"""
LeetCode: 2025 10 06 23.10.01 Accepted Runtime 0ms Memory 17.9MB

Algorithm:
TODO: Describe your approach here

Time Complexity: O(n)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
        
        if not list2:
            return list1

        dummy = ListNode()
        current = dummy

        while list1 and list2:

            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next

            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if not list1:
            current.next = list2

        elif not list2:
            current.next = list1

        return dummy.next