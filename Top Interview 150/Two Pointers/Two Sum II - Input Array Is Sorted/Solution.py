class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1

        while left < right:
            index_sum = numbers[left] + numbers[right]

            while index_sum > target:
                right -= 1
                index_sum = numbers[left] + numbers[right]

            if index_sum == target:
                return [left + 1, right + 1]

            left += 1

        return [left + 1, right + 1]
