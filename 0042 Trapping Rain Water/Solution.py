class Solution:
    def trap(self, height: list[int]) -> int:
        if len(height) < 3:
            return 0

        result = 0
        left = 0
        for i in range(len(height)):
            if height[i] >= height[left]:
                for val in height[left + 1 : i]:
                    result += height[left] - val
                left = i

        right = height[left:]
        right.reverse()
        result += self.trap(right)

        return result
