# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        que = deque([(root, 0)])
        avg_val = deque([0])
        count = 0
        curr_depth = 0

        while que:
            curr, depth = que.popleft()

            if depth == curr_depth:
                avg_val[-1] += curr.val
                count += 1
            else:
                avg_val[-1] = avg_val[-1] / count
                count = 1
                avg_val.append(curr.val)
                curr_depth = depth

            if curr.left:
                que.append((curr.left, depth + 1))
            if curr.right:
                que.append((curr.right, depth + 1))

        avg_val[-1] = avg_val[-1] / count

        return avg_val

