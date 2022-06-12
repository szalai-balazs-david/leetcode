class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if len(nums) < 3:
            return []

        result = []
        nums = sorted(nums)

        for i in range(len(nums) - 2):
            if i == 0 or nums[i] != nums[i-1]:
                for x in self.two_sum(nums[i+1:], -1 * nums[i]):
                    result.append([nums[i], x[0], x[1]])

        return result

    def two_sum(self, nums: list[int], target: int) -> list[list[int]]:
        dict = {}
        result = []
        for i in range(len(nums)):
            if nums[i] in dict:
                res = [nums[dict[nums[i]]], nums[i]]
                if res not in result:
                    result.append(res)
            else:
                dict[target - nums[i]] = i
        return result
