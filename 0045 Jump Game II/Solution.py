class Solution:
    def jump(self, nums: list[int]) -> int:
        print(nums)
        if len(nums) == 1:
            return 0
        if nums[0] >= len(nums) - 1:
            return 1

        def singleJump(index: int) -> int:
            best = 0
            best_index = index
            for i in range(1, nums[index] + 1):
                current = i + nums[i + index]
                if current >= best:
                    best = current
                    best_index = i + index
            return best_index

        i = 0
        count = 1
        while nums[i] < len(nums) - 1 - i:
            count += 1
            i = singleJump(i)

        return count
