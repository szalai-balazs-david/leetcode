class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        column_count = len(matrix[0])
        values = [[0] * column_count for i in range(column_count)]
        result = 0
        for row in matrix:
            start = None
            for j in range(len(row)):
                if row[j] == "1":
                    # Add all options between oldest 1 to this 1 to values
                    if start is None:
                        start = j
                        values[j][j] += 1
                    else:
                        # There was at least 1 one before this. Add all options ending with this node
                        for start_index in range(start, j + 1):
                            values[start_index][j] += 1
                else:
                    if start is None:
                        for end_index in range(j, column_count):
                            result = max(result, values[j][end_index] * (end_index - j + 1))
                            values[j][end_index] = 0
                    else:
                        # Remove options that are no longer valid, and evaluate result
                        for start_index in range(start, column_count):
                            for end_index in range(start_index, column_count):
                                if start_index <= j <= end_index and values[start_index][end_index] != 0:
                                    result = max(result, values[start_index][end_index] * (end_index - start_index + 1))
                                    values[start_index][end_index] = 0
                    # Lastly mark that no 1 was found prior
                    start = None

        for start_index in range(column_count):
            for end_index in range(start_index, column_count):
                if values[start_index][end_index] != 0:
                    result = max(result, values[start_index][end_index] * (end_index - start_index + 1))
        return result
