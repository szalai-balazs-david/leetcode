class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1] == 1:
            return 0
        grid = [[0]*len(obstacleGrid[0]) for i in range(len(obstacleGrid))]
        for i in range(0, len(obstacleGrid)):
            for j in range(0, len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    grid[i][j] = 0
                elif i == 0:
                    if j == 0:
                        grid[i][j] = 1
                    else:
                        grid[i][j] = grid[i][j-1]
                else:
                    if j == 0:
                        grid[i][j] = grid[i-1][j]
                    else:
                        grid[i][j] = grid[i-1][j] + grid[i][j-1]
        return grid[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]
