class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 1:
            return [nums]
        result = []

        x = nums[0]
        y = self.permute(nums[1:])
        for yy in y:
            arr = [x] + yy
            result.append(arr)
        for i in range(1, len(nums)-1):
            for yy in y:
                arr = yy[:i] + [x] + yy[i:]
                result.append(arr)
        for yy in y:
            arr = yy + [x]
            result.append(arr)
        return result
