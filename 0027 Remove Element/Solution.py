class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        nums.sort()
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < val:
                break
            if nums[i] == val:
                del nums[i]
        return len(nums)
