class Solution:
    def maxArea(self, height: List[int]) -> int:

        def calArea(point1, point2, height):
            min_height = min(height[point1], height[point2])
            length = point2 - point1

            return length * min_height

        left = 0
        right = len(height) - 1
        max_area = calArea(0, right, height)

        while left < right:
            curr_area = calArea(left, right, height)

            if curr_area > max_area:
                max_area = curr_area

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
