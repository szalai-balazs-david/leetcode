class Solution:
    def maxArea(self, height: list[int]) -> int:
        result = 0
        left = 0
        right = len(height) - 1
        max_height = -1

        while left < right:
            w = right - left
            h = min(height[left], height[right])
            if max_height == -1:
                max_height = h
                result = h * w
            elif h > max_height:
                result = max(result, h * w)

            if height[left] > height[right]:
                right -=1
            else:
                left += 1

        return result
