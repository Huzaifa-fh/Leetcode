class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        size = len(nums)
        curr_index = 0

        for i in range(size):
            if nums[i] != val:
                nums[curr_index] = nums[i]
                curr_index += 1

        return curr_index
