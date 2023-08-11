class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}

        def rob_helper(index):
            nonlocal memo

            if index >= len(nums):
                return 0
            if index in memo:
                return memo[index]

            result = max(rob_helper(index + 2) + nums[index], rob_helper(index + 1))
            memo[index] = result
            return result

        return rob_helper(0)
