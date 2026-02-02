"""
LeetCode: Reverse Linked List
Link: https://leetcode.com/problems/reverse-linked-list/

Pattern: Linked List (Pointer Manipulation)

Approach:
- Use three pointers: prev, curr, nxt.
- Traverse the list.
- Reverse the link direction at each step.
- Move pointers forward.
- Return prev as new head.

Time Complexity: O(n)
Space Complexity: O(1)
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
