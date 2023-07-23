# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        que = deque([(root, 0)])
        output = deque()

        while que:
            curr, curr_depth = que.popleft()

            if len(que) > 0:
                next_ele, next_depth = que[0]

                if next_depth > curr_depth:
                    output.append(curr.val)
            else:
                output.append(curr.val)

            if curr.left:
                que.append((curr.left, curr_depth + 1))
            if curr.right:
                que.append((curr.right, curr_depth + 1))

        return output
