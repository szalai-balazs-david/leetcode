class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        columns = len(matrix[0])
        l = 0
        r = columns * len(matrix)
        while l < r:
            mid = (l + r) // 2
            element = matrix[mid // columns][mid % columns]
            if element == target:
                return True
            if element < target:
                if mid == l:
                    return False
                l = mid
            else:
                r = mid
        return False
