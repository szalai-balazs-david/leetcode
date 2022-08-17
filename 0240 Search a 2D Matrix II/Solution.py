class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        def binary_search(low: int, high: int, nums: list[int]) -> bool:
            if low >= high:
                return nums[high] == target
            mid = low + (high - low) // 2
            mid_value = nums[mid]
            if mid_value == target:
                return True
            if mid_value > target:
                return binary_search(low, mid, nums)
            return binary_search(mid + 1, high, nums)

        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        high = len(matrix[0]) - 1
        for row in matrix:
            if binary_search(0, high, row):
                return True
        return False
