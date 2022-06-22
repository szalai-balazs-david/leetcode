class Solution:
    def trap(self, height: list[int]) -> int:
        if len(height) < 3:
            return 0

        result = 0
        left = 0
        right = len(height) - 1
        left_max = left
        right_max = right

        while left < right:
            if height[left] < height[right]:
                left += 1
                if height[left] >= height[left_max]:
                    for val in height[left_max:left + 1]:
                        result += max(0, height[left_max] - val)
                    left_max = left
            else:
                right -= 1
                if height[right] >= height[right_max]:
                    for val in height[right:right_max + 1]:
                        result += max(0, height[right_max] - val)
                    right_max = right

        return result
