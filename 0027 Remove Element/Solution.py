class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i - k] == val:
                del nums[i - k]
                k += 1
        return len(nums)
