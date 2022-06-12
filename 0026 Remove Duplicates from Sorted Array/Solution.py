class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        start = 0
        while True:
            done = True
            for i in range(start, len(nums) - 1):
                if nums[i] == nums[i + 1]:
                    done = False
                    del nums[i + 1]
                    start = i
                    break
            if done:
                break
        return len(nums)
