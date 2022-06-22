class Solution:
    def trap(self, height: list[int]) -> int:
        if len(height) < 3:
            return 0
        i_max = height.index(max(height))
        result = self.trapLeft(height[:i_max + 1]) + self.trapRight(height[i_max:])

        return result

    def trapRight(self, height: list[int]) -> int:
        if len(height) < 3:
            return 0

        result = 0
        right = len(height) - 1
        for i in range(len(height)-1, -1, -1):
            if height[i] >= height[right]:
                print(height[i])
                for val in height[i + 1 : right]:
                    result += height[right] - val
                right = i

        return result

    def trapLeft(self, height: list[int]) -> int:
        if len(height) < 3:
            return 0

        result = 0
        left = 0
        for i in range(len(height)):
            if height[i] >= height[left]:
                for val in height[left + 1 : i]:
                    result += height[left] - val
                left = i

        return result
