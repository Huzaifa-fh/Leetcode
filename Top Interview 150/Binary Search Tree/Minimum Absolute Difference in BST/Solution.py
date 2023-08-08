# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        prev = None
        result = float('inf')

        def dfs(root: Optional[TreeNode]):
            if root is None:
                return

            nonlocal prev, result

            dfs(root.left)

            if prev:
                result = min(result, abs(root.val - prev.val))
            prev = root

            dfs(root.right)

        dfs(root)

        return result
