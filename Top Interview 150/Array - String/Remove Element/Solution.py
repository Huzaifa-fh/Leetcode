class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        original_length = len(nums)

        while True:
            try:
                nums.remove(val)
                count += 1
            except ValueError:
                break

        k = original_length - count

        return k
