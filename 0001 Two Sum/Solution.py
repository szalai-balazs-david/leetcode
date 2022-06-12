class Solution:
    def two_sum_old(self, nums: list[int], target: int) -> list[int]:
        for x in range(len(nums) - 1):
            for y in range(x + 1, len(nums)):
                if nums[x] + nums[y] == target:
                    return [x, y]
        raise Exception("No solution was found")

    def two_sum(self, nums: list[int], target: int) -> list[int]:
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                return [dict[nums[i]], i]
            else:
                dict[target - nums[i]] = i
        raise Exception("No solution was found")
