class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        l_index = 1

        for i in range(2, len(nums)):
            if nums[l_index - 1] != nums[i]:
                l_index += 1
                nums[l_index] = nums[i]

        k = l_index + 1

        return k
