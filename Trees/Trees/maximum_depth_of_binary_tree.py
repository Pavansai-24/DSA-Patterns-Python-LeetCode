"""
LeetCode: Maximum Depth of Binary Tree
Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

Pattern: Binary Tree + Recursion (DFS)

Approach:
- If root is None, return 0.
- Recursively compute depth of left subtree.
- Recursively compute depth of right subtree.
- Return 1 + maximum of left and right depths.

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
    def maxDepth(self, root):
        if not root:
            return 0
        lefth=self.maxDepth(root.left)
        righth=self.maxDepth(root.right)
        return 1+max(lefth,righth)
