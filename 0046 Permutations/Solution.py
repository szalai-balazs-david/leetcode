class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 1:
            return [nums]
        result = []

        x = nums[0]
        y = self.permute(nums[1:])
        for i in range(len(nums)):
            for yy in y:
                arr = yy[:i] + [x] + yy[i:]
                result.append(arr)
        return result
