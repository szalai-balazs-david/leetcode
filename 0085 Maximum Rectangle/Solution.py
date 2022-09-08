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
            mem = [(0, row[0])]
            for i in range(1, columns):
                if not mem or row[i] > mem[-1][1]:
                    mem.append((i, row[i]))
                else:
                    while mem and mem[-1][1] >= row[i]:
                        j, h = mem.pop()
                        result = max(result, h * (i-j))
                    mem.append((j, row[i]))
            while mem:
                j, h = mem.pop()
                result = max(result, h * (columns - j))

        return result
