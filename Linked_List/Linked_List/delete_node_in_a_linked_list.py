"""
LeetCode: Delete Node in a Linked List
Link: https://leetcode.com/problems/delete-node-in-a-linked-list/

Pattern: Linked List

Approach:
Since we are not given access to the head of the list,
we copy the value of the next node into the current node
and move forward until the last node.
Finally, we remove the last duplicated node.

Time Complexity: O(n)
Space Complexity: O(1)
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prev=None
        while node is not None and node.next is not None:
            node.val=node.next.val
            prev=node
            node=node.next
        prev.next=None
