class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        pivot = self.find_pivot(nums)
        if pivot == -1:
            values = nums.copy()
        else:
            values = nums[pivot + 1:] + nums[:pivot + 1]

        if values[0] > target or values[-1] < target:
            return -1

        left = 0
        right = len(values) - 1
        while True:
            if left == right:
                result = left + 1 + pivot
                if result >= len(nums):
                    result -= len(nums)
                return result if values[left] == target else -1

            half = int((right + 1 + left) / 2)
            if values[half - 1] < target:
                if values[half] > target:
                    return -1
                left = half
            else:
                right = half - 1

    def find_pivot(self, nums: list[int]) -> int:
        if nums[0] < nums[-1]:
            return -1

        left = 0
        right = len(nums) - 1

        while True:
            half = int((right + 1 + left) / 2)
            if nums[left] <= nums[half - 1] and nums[half] <= nums[-1]:
                return half - 1
            elif nums[left] <= nums[half - 1]:
                left = half
            else:
                right = half - 1
