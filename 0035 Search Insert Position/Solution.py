class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 0 if nums[0] >= target else 1

        mid = int(len(nums) / 2)
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            return self.searchInsert(nums[:mid], target)
        return mid + self.searchInsert(nums[mid:], target)
