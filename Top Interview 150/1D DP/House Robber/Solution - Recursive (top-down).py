class Solution:
    def rob(self, nums: List[int]) -> int:

        def rob_helper(index):
            if index >= len(nums):
                return 0

            return max(rob_helper(index + 2) + nums[index], rob_helper(index + 1))

        return rob_helper(0)
