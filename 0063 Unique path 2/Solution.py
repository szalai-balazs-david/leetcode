class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1] == 1:
            return 0
        grid = [[0]*len(obstacleGrid[0]) for i in range(len(obstacleGrid))]

        grid[0][0] = 1 - obstacleGrid[0][0]
        for i in range(1, len(obstacleGrid)):
            grid[i][0] = 0 if grid[i-1][0] == 0 else 1 - obstacleGrid[i][0]
        for j in range(1, len(obstacleGrid[0])):
            grid[0][j] = 0 if grid[0][j-1] == 0 else 1 - obstacleGrid[0][j]

        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    grid[i][j] = 0
                else:
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]
        return grid[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]
