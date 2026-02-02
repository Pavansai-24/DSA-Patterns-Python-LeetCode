"""
LeetCode: Merge Two Sorted Lists
Link: https://leetcode.com/problems/merge-two-sorted-lists/

Pattern: Linked List (Merging Technique + Dummy Node)

Approach:
- Create a dummy node to simplify edge cases.
- Use pointer l3 to build the merged list.
- Compare values of l1 and l2.
- Attach the smaller node to l3.
- Move pointers forward.
- Attach remaining nodes at the end.

Time Complexity: O(n + m)
Space Complexity: O(1)
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        l3 = dummy
        while l1 and l2:
            if l1.val < l2.val:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next
            l3 = l3.next
        if l1:
            l3.next = l1
        elif l2:
            l3.next = l2
        return dummy.next
