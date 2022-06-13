class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        pivot = self.unrotate(nums)
        if pivot == -1:
            values = nums.copy()
        else:
            values = nums[pivot + 1:] + nums[:pivot + 1]

        if values[0] > target or values[-1] < target:
            return -1

        result = 0
        while True:
            if len(values) == 1:
                result = result + 1 + pivot
                if result >= len(nums):
                    result -= len(nums)
                return result if values[0] == target else -1
            half = int(len(values) / 2)
            x = values[:half]
            y = values[half:]
            if x[-1] == target:
                result = result + len(x) + pivot
                if result >= len(nums):
                    result -= len(nums)
                return result
            if x[-1] < target:
                if y[0] > target:
                    return -1
                result += len(x)
                values = y
            else:
                values = x

    def unrotate(self, nums: list[int]) -> int:
        if nums[0] < nums[-1]:
            return -1

        values = nums.copy()
        pivot = 0

        while True:
            half = int(len(values) / 2)
            x = values[:half]
            y = values[half:]
            if x[0] <= x[-1] and y[0] <= y[-1]:
                pivot += len(x)
                break
            elif x[0] <= x[-1]:
                pivot += len(x)
                values = y
            else:
                values = x

        return pivot - 1
