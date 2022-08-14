class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        h = len(grid)
        w = len(grid[0])

        for i in range(w-2,-1,-1):
            grid[-1][i] = grid[-1][i+1] + grid[-1][i]
        for i in range(h-2,-1,-1):
            grid[i][-1] = grid[i+1][-1] + grid[i][-1]

        for i in range(2, min(h,w)+1):
            grid[-i][-i] = grid[-i][-i] + min(grid[-i][-(i-1)], grid[-(i-1)][-i])
            for j in range(w-i-1, -1, -1):
                grid[-i][j] = grid[-i][j] + min(grid[-i][j+1], grid[-(i-1)][j])
            for j in range(h-i-1,-1,-1):
                grid[j][-i] = grid[j][-i] + min(grid[j+1][-i], grid[j][-(i-1)])

        return grid[0][0]
