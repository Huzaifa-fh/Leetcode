class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_map = {}

        for i in range(len(nums)):
            to_find = target - nums[i]
            if to_find in num_map:
                return [num_map[to_find], i]
            num_map[nums[i]] = i

        return []
