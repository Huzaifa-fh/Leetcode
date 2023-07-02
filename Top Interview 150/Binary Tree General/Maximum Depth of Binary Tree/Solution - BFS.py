from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root: return 0

        que = deque()
        que.append((root, 1))
        max_depth = 0

        while que:
            node, depth = que.popleft()

            max_depth = max(max_depth, depth)

            if node.left:
                que.append((node.left, depth + 1))
            if node.right:
                que.append((node.right, depth + 1))

        return max_depth
