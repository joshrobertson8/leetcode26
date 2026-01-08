"""
LeetCode: 2024 10 31 11.41.09 Accepted Runtime 0ms Memory 11.5mb

Problem:
class ListNode:
def __init__(self, val=0, next=None):
self.val = val
self.next = next

Algorithm:
Use dummy node to simplify edge cases. Handle empty lists first. Compare heads of both lists, append smaller to current, advance that list. After loop, append remaining nodes from the non-empty list. Return dummy.next (skip dummy node).

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def mergeTwoLists(self, list1, list2):
        
        dummy = ListNode(1)
        current = dummy
        
        if not list1:
            return list2
        if not list2:
            return list1

        
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