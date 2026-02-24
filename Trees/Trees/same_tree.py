"""
LeetCode: Same Tree
Link: https://leetcode.com/problems/same-tree/

Pattern: Binary Tree + Recursion (DFS)

Approach:
- If both nodes are None → return True.
- If one is None → return False.
- If values differ → return False.
- Recursively check left and right subtrees.

Time Complexity: O(n)
Space Complexity: O(h)  # h = height of tree (recursion stack)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p, q):
        def same(root1, root2):
            if root1 is None and root2 is None:
                return True
            if root1 is None or root2 is None:
                return False
            if root1.val != root2.val:
                return False
            return same(root1.left, root2.left) and same(root1.right, root2.right)

        return same(p, q)
