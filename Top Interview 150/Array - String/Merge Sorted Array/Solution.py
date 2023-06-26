class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        i = 0
        count = 0

        def move_one_up(num1, index, m, count):
            for i in range(m - 1 + count, index - 1, -1):
                num1[i], num1[i + 1] = num1[i + 1], num1[i]

        while i < m + n and j < n:
            if nums1[i] <= nums2[j]:
                if i < m + count:
                    i += 1
                else:
                    nums1[i] = nums2[j]
                    i += 1
                    j += 1
                    count += 1
            elif nums1[i] > nums2[j]:
                move_one_up(nums1, i, m, count)
                nums1[i] = nums2[j]
                i += 1
                j += 1
                count += 1


