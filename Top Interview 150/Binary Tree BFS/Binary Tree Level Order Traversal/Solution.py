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
        ordered_nodes = []
        level_ordered_nodes = []
        curr_depth = 0

        while que:
            curr, depth = que.popleft()

            if depth == curr_depth:
                ordered_nodes.append(curr.val)
            else:
                level_ordered_nodes.append(ordered_nodes)
                ordered_nodes = [curr.val]
                curr_depth = depth

            if curr.left:
                que.append((curr.left, depth + 1))
            if curr.right:
                que.append((curr.right, depth + 1))

        level_ordered_nodes.append(ordered_nodes)

        return level_ordered_nodes

