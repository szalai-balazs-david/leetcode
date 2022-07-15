class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []
        h = len(matrix)
        w = len(matrix[0])

        for i in range(min(h + 1, w + 1) // 2):
            result += matrix[i][i:w-i]
            for j in range(i + 1, h - 1 - i):
                result.append(matrix[j][-1-i])
            if i != h - i - 1:
                last_row = matrix[-1-i][i:w-i]
                last_row.reverse()
                result += last_row
            if i != w - i - 1:
                for j in range(h - 2 - i, i, -1):
                    result.append(matrix[j][i])

        return result
