class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        sum_ = 0
        min_len = float('inf')


        for right in range(len(nums)):
            sum_ += nums[right]

            while sum_ >= target:
                min_len = min(min_len, right - left + 1)
                sum_ -=nums[left]
                left += 1

        if min_len == float('inf'):
            return 0

        return min_len
