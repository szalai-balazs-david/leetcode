class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        rows = len(matrix)
        columns = len(matrix[0])
        values = [[0] * columns for i in range(rows)]
        for i in range(rows):
            for j in range(columns):
                values[i][j] = 0 if matrix[i][j] == "0" else (values[i][j-1] + 1) if j > 0 else 1

        result = 0
        for i in range(rows - 1, -1, -1):
            for j in range(columns):
                if values[i][j] == 0:
                    continue
                width = values[i][j]
                current_best = 0
                for k in range(i, -1, -1):
                    # Only do calc if width decreased
                    if values[k][j] < width:
                        current_best = max(current_best, (i - k) * width)
                        width = values[k][j]
                        # If there's no way to beat current_best with this width, stop looping
                        if width * (i + 1) <= current_best:
                            break
                current_best = max(current_best, (i + 1) * width)
                values[i][j] = current_best
                result = max(result, current_best)

        return result
