class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        n = len(nums)

        count_map = {}

        for i in range(n):
            if nums[i] in count_map:
                count_map[nums[i]] += 1
            else:
                count_map[nums[i]] = 1

        max_value = max(count_map.items(), key=lambda x: x[1])

        return max_value[0]
