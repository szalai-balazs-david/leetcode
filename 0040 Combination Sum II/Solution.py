class Solution:
    #cheating: I looked at solution, then tried to recreate it
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:

        def backtrack(combination: list[int], result: list[list[int]], i: int, remainder: int):
            if remainder == 0:
                result.append(list(combination))
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                remainder = remainder - candidates[j]
                if remainder < 0:
                    break
                combination.append(candidates[j])
                backtrack(combination, result, j + 1, remainder)
                combination.pop()
                remainder += candidates[j]

        candidates.sort()
        results = []
        comb = []

        backtrack(comb, results, 0, target)

        return results