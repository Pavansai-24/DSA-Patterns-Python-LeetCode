"""
LeetCode: Middle of the Linked List
Link: https://leetcode.com/problems/middle-of-the-linked-list/

Pattern: Linked List + Fast & Slow Pointers

Approach:
Use two pointers:
- Slow pointer moves one step at a time.
- Fast pointer moves two steps at a time.

When the fast pointer reaches the end,
the slow pointer will be at the middle.

Time Complexity: O(n)
Space Complexity: O(1)
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def middleNode(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
