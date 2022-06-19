class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for row in board:
            if not self.isValidGroup(row):
                return False
        for i in range(9):
            column = []
            for x in range(9):
                column.append(board[x][i])
            if not self.isValidGroup(column):
                return False
        for i in range(3):
            for j in range(3):
                group = []
                for x in range(3):
                    for y in range(3):
                        group.append(board[i * 3 + x][j * 3 + y])
                if not self.isValidGroup(group):
                    return False

        return True

    def isValidGroup(self, nums: list[int]) -> bool:
        found = []
        for x in nums:
            if x == ".":
                continue
            if x in found:
                return False
            found.append(x)

        return True
