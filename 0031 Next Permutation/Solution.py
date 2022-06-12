class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        last_increasing = -1
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                last_increasing = i

        if last_increasing == -1:
            nums.sort()
            return

        elements = nums[last_increasing:]

        if len(elements) == 2:
            nums[last_increasing] = elements[1]
            nums[last_increasing + 1] = elements[0]
            return

        old = elements[0]
        new = elements[1]
        for e in elements[2:]:
            if new - old > e - old > 0:
                new = e
        nums[last_increasing] = new

        elements.remove(new)
        elements.sort()
        for i in range(last_increasing + 1, len(nums)):
            nums[i] = elements[i - (last_increasing + 1)]
