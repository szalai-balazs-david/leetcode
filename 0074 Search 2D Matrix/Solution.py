class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        def binary_search(low: int, high: int, column_count: int) -> bool:
            # Check base case
            if high >= low:

                mid = (high + low) // 2
                row = mid // column_count
                column = mid % column_count

                # If element is present at the middle itself
                if matrix[row][column] == target:
                    return True

                # If element is smaller than mid, then it can only
                # be present in left subarray
                elif matrix[row][column] > target:
                    return binary_search(low, mid - 1, column_count)

                # Else the element can only be present in right subarray
                else:
                    return binary_search(mid + 1, high, column_count)

            else:
                # Element is not present in the array
                return False

        columns = len(matrix[0])
        elements = len(matrix) * columns
        return binary_search(0, elements - 1, columns)
