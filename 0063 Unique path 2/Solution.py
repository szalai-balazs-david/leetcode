class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1] == 1:
            return 0
        grid = [[0]*len(obstacleGrid[0]) for i in range(len(obstacleGrid))]

        for i in range( len(obstacleGrid)):
            if obstacleGrid[i][0] == 1:
                break
            else:
                grid[i][0] = 1
        for j in range(len(obstacleGrid[0])):
            if obstacleGrid[0][j] == 1:
                break
            else:
                grid[0][j] = 1

        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    grid[i][j] = 0
                else:
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]
        return grid[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]
