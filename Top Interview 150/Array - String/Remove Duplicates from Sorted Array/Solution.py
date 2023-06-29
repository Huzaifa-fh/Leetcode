class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        l_index = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[l_index]:
                l_index += 1
                nums[l_index] = nums[i]

        k = l_index + 1

        return k
