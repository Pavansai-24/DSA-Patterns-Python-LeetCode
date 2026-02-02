"""
LeetCode: Delete the Middle Node of a Linked List
Link: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

Pattern: Linked List + Fast & Slow Pointers

Approach:
- Use two pointers (slow and fast).
- Move slow one step and fast two steps.
- Keep track of the previous node of slow.
- When fast reaches the end, slow will be at the middle.
- Remove the middle node by adjusting prev.next.

Time Complexity: O(n)
Space Complexity: O(1)
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head.next==None:
            return None
        slow=fast=head
        prev=None
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=slow.next
        return head
