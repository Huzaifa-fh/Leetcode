# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        que = deque([(root, 0)])
        level_ordered_nodes = []

        while que:
            curr, depth = que.popleft()

            if depth == len(level_ordered_nodes):
                level_ordered_nodes.append([])

            level_ordered_nodes[depth].append(curr.val)

            if curr.left:
                que.append((curr.left, depth + 1))
            if curr.right:
                que.append((curr.right, depth + 1))

        return level_ordered_nodes

