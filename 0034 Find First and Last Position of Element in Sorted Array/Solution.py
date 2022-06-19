class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if len(nums) == 0 or target > nums[-1] or target < nums[0]:
            return [-1, -1]

        first = self.find_first(nums, target)
        if first == -1:
            return [-1, -1]

        return [first, self.find_last(nums, target)]

    def find_first(self, nums: list[int], target) -> int:
        if nums[0] == target:
            return 0

        left = 0
        right = len(nums) - 1
        mid_prev = -1

        while left < right:
            mid = int((left + right + 1) / 2)
            if nums[mid] == target and nums[mid - 1] != target:
                return mid
            if nums[mid] >= target:
                right = mid
            else:
                left = mid
            if mid_prev == mid:
                return -1
            mid_prev = mid

    def find_last(self, nums: list[int], target) -> int:
        if nums[-1] == target:
            return len(nums) - 1

        left = 0
        right = len(nums) - 1
        mid_prev = -1

        while left < right:
            mid = int((left + right) / 2)
            if nums[mid] == target and nums[mid + 1] != target:
                return mid
            if nums[mid] <= target:
                left = mid
            else:
                right = mid
            if mid_prev == mid:
                return -1
            mid_prev = mid
