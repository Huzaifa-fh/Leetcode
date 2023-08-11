class Solution:
    def rob(self, nums: List[int]) -> int:

        last = 0
        second_last = 0

        for i in range(len(nums)):
            temp = last
            last = max(second_last + nums[i], last)

            second_last = temp

        return last
