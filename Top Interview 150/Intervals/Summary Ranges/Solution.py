class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        size = len(nums)
        if size == 0: return []

        ranges = []
        prev = start = end = nums[0]

        for i in range(1, size):
            if nums[i] == prev + 1:
                end = nums[i]
            else:
                ranges.append(str(start) if start == end else f"{start}->{end}")
                start = end = nums[i]

            prev = nums[i]

        ranges.append(str(start) if start == end else f"{start}->{end}")
        return ranges

