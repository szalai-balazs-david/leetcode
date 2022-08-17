class Solution:
    def findMin(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return min(nums)
        def binary_search(low: int, high: int) -> int:
            if low >= high:
                return nums[high]

            mid = (low + high) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid] == nums[low] and nums[mid] == nums[high]:
                return min(binary_search(mid + 1, high), binary_search(low, mid))
            if nums[mid] == nums[high] and nums[mid] > nums[low]:
                return nums[low]
            if nums[mid] > nums[high]:
                return binary_search(mid + 1, high)
            return binary_search(low, mid)

        return binary_search(0, len(nums) - 1)

