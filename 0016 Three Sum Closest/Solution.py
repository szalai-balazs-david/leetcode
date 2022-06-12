class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)

        nums.sort()
        result = nums[0] + nums[1] + nums[len(nums) - 1]

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if target == s:
                    return s
                if abs(target - result) > abs(target - s):
                    result = s
                if target < s:
                    right -= 1
                else:
                    left += 1
        return result
