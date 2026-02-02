"""
LeetCode: Linked List Cycle
Link: https://leetcode.com/problems/linked-list-cycle/

Pattern: Linked List + Fast & Slow Pointers (Floyd’s Algorithm)

Approach:
- Use two pointers: slow and fast.
- Slow moves one step.
- Fast moves two steps.
- If they ever meet, a cycle exists.
- If fast reaches the end, no cycle exists.

Time Complexity: O(n)
Space Complexity: O(1)
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False
