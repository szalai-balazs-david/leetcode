class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if 0 not in nums:
            return True
        nums.reverse()
        return self.test(nums[1:], 0)

    def test(self, nums: list[int], start: int) -> bool:
        try:
            index = nums.index(0, start)
            canDo = False
            for i in range(index + 1, len(nums), 1):
                if nums[i] > i - index:
                    canDo = True
                    break
            if not canDo:
                return False

            return self.test(nums, index + 1)
        except:
            return True
