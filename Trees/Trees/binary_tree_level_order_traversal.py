"""
LeetCode: Binary Tree Level Order Traversal
Link: https://leetcode.com/problems/binary-tree-level-order-traversal/

Pattern: Binary Tree + BFS (Queue)

Approach:
- If root is None, return empty list.
- Use a queue to process nodes level by level.
- For each level:
    - Record current queue size.
    - Process exactly that many nodes.
    - Add children to queue.
- Append level values to answer.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        ans=[]
        queue=deque([root])
        while queue:
            n=len(queue)
            level=[]
            for i in range(n):
                node=queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(level)
        return ans
