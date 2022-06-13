class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        left = 0
        right = len(nums) - 1

        while left < right:
            half = int((right + 1 + left) / 2)
            if nums[left] <= nums[half - 1]: # left side is ascending
                if nums[left] <= target <= nums[half - 1]: # left side has target
                    right = half - 1
                else:
                    left = half
            else: # right side is ascending
                if nums[half] <= target <= nums[right]: # right side has target
                    left = half
                else:
                    right = half - 1

        return left if nums[left] == target else -1
