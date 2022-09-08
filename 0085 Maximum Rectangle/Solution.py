class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        rows = len(matrix)
        columns = len(matrix[0])
        values = [[0] * columns for i in range(rows)]
        for i in range(rows):
            for j in range(columns):
                values[i][j] = 0 if matrix[i][j] == "0" else (values[i-1][j] + 1) if i > 0 else 1

        result = 0
        for row in values:
            for j in range(columns):
                if row[j] == 0:
                    continue
                height = row[j]
                largest_area = 0
                for k in range(j, -1, -1):
                    # Only do calc if height decreased
                    if row[k] >= height:
                        continue
                    largest_area = max(largest_area, (j - k) * height)
                    height = row[k]
                    # If there's no way to beat current_best with this width, stop looping
                    if height * (j + 1) <= largest_area:
                        break
                largest_area = max(largest_area, (j + 1) * height)
                result = max(result, largest_area)

        return result
