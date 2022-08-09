class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        h = len(grid)
        w = len(grid[0])
        result = [[0] * w for i in range(h)]

        result[-1][-1] = grid[-1][-1]
        for i in range(w-2,-1,-1):
            result[-1][i] = result[-1][i+1] + grid[-1][i]
        for i in range(h-2,-1,-1):
            result[i][-1] = result[i+1][-1] + grid[i][-1]

        for i in range(2, min(h,w)+1):
            result[-i][-i] = grid[-i][-i] + min(result[-i][-(i-1)], result[-(i-1)][-i])
            for j in range(w-i-1, -1, -1):
                result[-i][j] = grid[-i][j] + min(result[-i][j+1], result[-(i-1)][j])
            for j in range(h-i-1,-1,-1):
                result[j][-i] = grid[j][-i] + min(result[j+1][-i], result[j][-(i-1)])

        return result[0][0]
