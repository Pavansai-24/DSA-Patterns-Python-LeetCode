"""
LeetCode: Invert Binary Tree
Link: https://leetcode.com/problems/invert-binary-tree/

Pattern: Binary Tree + DFS (Recursion)

Approach:
- Use a helper function solve().
- If node is None, return.
- Swap left and right children.
- Recursively invert left and right subtrees.
- Return root.

Time Complexity: O(n)
Space Complexity: O(h)  # recursion stack
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def invertTree(self, root):
        def solve(node):
            if not node:
                return
            node.left,node.right=node.right,node.left
            solve(node.left)
            solve(node.right)

        solve(root)
        return root
