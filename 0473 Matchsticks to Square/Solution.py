class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        target = total // 4

        matchsticks.sort()
        if matchsticks[0] > target:
            return False
        
        def backtrack(sums: list[int], index: int):
            for i in range(4):
                if sums[i] + matchsticks[index] <= target:
                    sums[i] += matchsticks[index]
                    if index == 0:
                        return True
                    if backtrack(sums, index - 1):
                        return True
                    sums[i] -= matchsticks[index]
            return False

        return backtrack([0,0,0,0], len(matchsticks) - 1)
