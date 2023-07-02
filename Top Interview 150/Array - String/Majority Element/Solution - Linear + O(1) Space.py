class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count = 0
        candidate = 0

        for num in nums:
            if count == 0:
                candidate = num

            if candidate == num:
                count += 1
            elif candidate != nums:
                count -= 1

        return candidate
