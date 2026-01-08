"""
LeetCode #0: , next=none):

Problem:
Definition for singly-linked list.
class ListNode(object):
def __init__(self, val=0, next=None):
self.val = val
self.next = next

Algorithm:
Traverse list and collect all values into array. Create reversed array. Compare original and reversed arrays. If equal, list is palindrome. This uses O(n) extra space but is straightforward.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def isPalindrome(self, head):
        current = head
        arr = []

        while current:
            arr.append(current.val)
            current = current.next
        
        r_arr = arr[::-1]

        if r_arr == arr:
            return True
        return False