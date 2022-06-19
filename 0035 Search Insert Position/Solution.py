class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if nums[0] >= target:
            return 0
        if nums[-1] < target:
            return len(nums)
        if nums[-1] == target:
            return len(nums) - 1

        left = 0
        right = len(nums) - 1

        while True:
            mid = int((left + right + 1) / 2)
            if nums[mid] >= target > nums[mid - 1]:
                return mid
            if nums[mid] > target:
                right = mid
            else:
                left = mid
